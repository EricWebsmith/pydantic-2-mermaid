from types import ModuleType
from typing import Any, Dict, get_args, get_origin, List, Set, Type

from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.fields import FieldInfo

from pydantic_mermaid.models import MermaidClass, MermaidGraph, Property


base_types = [str, int, float, bool]


def _get_name(v: Type[Any]) -> str:
    """get name from type"""
    if v in base_types:
        return v.__name__

    origin = get_origin(v)
    if origin is None:
        return v.__name__
    else:
        origin_name = origin.__name__
        sub_names = [_get_name(sub_type) for sub_type in get_args(v)]
        return f"{origin_name}[{', '.join(sub_names)}]"


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


class PydanticParser:
    """parse pydantic module to mermaid graph"""

    def __call__(self, module: ModuleType) -> MermaidGraph:
        graph = MermaidGraph()

        for class_name, class_type in module.__dict__.items():
            if class_name in ["BaseModel"]:
                continue

            properties: List[Property] = []

            if not isinstance(class_type, ModelMetaclass):
                continue

            model_type: Type[BaseModel] = class_type  # type: ignore
            # inheritance
            parents = model_type.mro()
            first_parent = parents[1]
            parent_name = first_parent.__name__
            graph.child_parents[class_name] = {parent_name}
            if parent_name in graph.classes:
                if parent_name not in graph.parent_children:
                    graph.parent_children[parent_name] = set()
                graph.parent_children[parent_name].add(class_name)

            # fields
            fields: Dict[str, FieldInfo] = model_type.model_fields
            graph.service_clients[class_name] = set()
            for field_name, field in fields.items():
                if field.annotation is None:  # pragma: no cover
                    continue

                field_type_name = _get_name(field.annotation)

                properties.append(Property(name=field_name, type=field_type_name))
                # dependencies
                graph.service_clients[class_name] = graph.service_clients[class_name] | _get_dependencies(field.annotation)

            graph.service_clients[class_name] = graph.service_clients[class_name]
            graph.classes[class_name] = MermaidClass(name=class_name, properties=properties)

        return graph
