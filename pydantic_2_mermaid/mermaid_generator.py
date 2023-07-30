from types import ModuleType
from typing import Any, Dict, List, Set, Type, get_args, get_origin
from pydantic import BaseModel

from pydantic.fields import FieldInfo
from pydantic._internal._model_construction import ModelMetaclass

from pydantic_2_mermaid.models import MermaidClass, Property, Relations


base_types = [str, int, float, bool]
# constrained types are generated dynamically we can only remove them by name
constrained_types = {
    "ConstrainedStrValue",
    "ConstrainedFloatValue",
    "ConstrainedIntValue",
    "ConstrainedSetValue",
    "ConstrainedFrozenSetValue",
    "ConstrainedListValue",
    "ConstrainedDecimalValue",
    "ConstrainedDateValue",
}


def _get_name(v: Type[Any]) -> str:
    """get name from type"""
    if v in base_types:
        return v.__name__

    origin = get_origin(v)
    if origin is None:
        return v.__name__

    if origin is not None:
        origin_name = origin.__name__
        sub_names = []
        for sub_type in get_args(v):
            sub_names.append(_get_name(sub_type))
        return f"{origin_name}[{', '.join(sub_names)}]"

    if "__name__" in dir(v):
        return v.__name__

    return str(v)


def _get_dependencies(v: Type[Any]) -> Set[str]:
    """get dependencies from property types"""
    ans: Set[str] = set()

    if v in base_types:
        return ans

    origin = get_origin(v)

    if origin is None:
        ans.add(v.__name__)

    if origin is not None:
        for sub_v in get_args(v):
            ans |= _get_dependencies(sub_v)

    return ans


class MermaidGenerator:
    """genertate a class chart from module"""

    def __init__(self, module: ModuleType) -> None:
        self.class_dict: Dict[str, MermaidClass] = {}
        # In computer science, a class that a dependent class depends on is called a dependency or `service`` class.
        # The dependent class is called the `client`` class.
        # The `service`` class provides `service` to the `client` class
        self.service_clients: Dict[str, Set[str]] = {}
        self.client_services: Dict[str, Set[str]] = {}
        self.parent_children: Dict[str, Set[str]] = {}
        self.child_parents: Dict[str, Set[str]] = {}
        self.allow_list: Set[str] = set()
        self.parse(module)

    def parse(self, module: ModuleType) -> None:
        """extrac information from module"""
        class_set: Set[str] = set()
        for class_name, class_type in module.__dict__.items():
            if class_name in ["BaseModel"]:
                continue

            properties: List[Property] = []

            if isinstance(class_type, ModelMetaclass):
                model_type: Type[BaseModel] = class_type  # type: ignore
                # inheritance
                parents = model_type.mro()
                first_parent = parents[1]
                parent_name = first_parent.__name__
                self.child_parents[class_name] = {parent_name}
                if parent_name in class_set:
                    if parent_name not in self.parent_children:
                        self.parent_children[parent_name] = set()
                    self.parent_children[parent_name].add(class_name)

                # fields
                fields: Dict[str, FieldInfo] = model_type.model_fields
                self.service_clients[class_name] = set()
                for field_name, field in fields.items():
                    if field.annotation is None:
                        continue

                    field_type_name = _get_name(field.annotation)

                    properties.append(Property(name=field_name, type=field_type_name))
                    # dependencies
                    self.service_clients[class_name] = self.service_clients[class_name] | _get_dependencies(
                        field.annotation)

                self.service_clients[class_name] = self.service_clients[class_name] & class_set
                class_set.add(class_name)
                self.class_dict[class_name] = MermaidClass(name=class_name, properties=properties)

    def generate_allow_list(self, root: str) -> None:
        """
        user can focus on certain class `root` and prune classes that is inherited from `root`
        or not a dependencies of `root`
        """
        self.allow_list = {root}
        if root != "":
            keys = list(self.service_clients.keys())
            keys.reverse()
            for dependant in keys:
                if dependant in self.allow_list:
                    self.allow_list = self.allow_list | self.service_clients[dependant]
        else:
            self.allow_list = {class_name for class_name in self.class_dict}

    def generate_dependencies(self) -> str:
        """print dependencies for class chart"""
        s = ""
        for dependant, depended in self.service_clients.items():
            if dependant not in self.allow_list:
                continue

            for d in depended:
                if d not in self.allow_list:
                    continue
                s += f"    {dependant} ..> {d}\n"

        s += "\n"
        return s

    def generate_inheritance(self) -> str:
        """print inheritance for class chart"""
        s = ""
        for parent, children in self.parent_children.items():
            for child in children:
                s += f"    {parent} <|-- {child}\n"
        return s

    def generate_chart(self, *, root: str = "", relations: Relations = Relations.Dependency) -> str:
        """print class chart"""
        self.generate_allow_list(root)

        s = "```mermaid\nclassDiagram"
        for class_name, class_type in self.class_dict.items():
            if class_name not in self.allow_list:
                continue

            parent_class_name = ""
            if class_name in self.child_parents:
                parent_class_name = list(self.child_parents[class_name])[0]
            if parent_class_name in self.allow_list:
                inherited_properties = {p.name for p in self.class_dict[parent_class_name].properties}
                s += class_type.generate_class(exclude=inherited_properties)
            else:
                s += str(class_type)

        s += "\n\n"

        if Relations.Dependency in relations:
            s += self.generate_dependencies()

        if Relations.Inheritance in relations:
            s += self.generate_inheritance()

        s += "```"
        return s
