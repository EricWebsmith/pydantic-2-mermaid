"""Parse pydantic 2.10 module to mermaid graph"""

from enum import EnumMeta
from types import ModuleType
from typing import Any, Dict, List, Set, Type, get_args, get_origin

from pydantic import BaseModel

# ModelMetaclass is commonly used pydantic related packages, and we need to import it here
# We use this to determine if a class is a pydantic model
# I am strongly against making it _internal
from pydantic._internal._model_construction import ModelMetaclass
from pydantic.fields import FieldInfo

from pydantic_mermaid.models import MermaidClass, MermaidGraph, Property

NoneType = type(None)  # There is no NoneType in python 3.8
base_types = [str, int, float, bool]


def type_normalize(type_name: str) -> str:
    if type_name == "NoneType":
        return "None"

    if type_name == "UnionType":
        return "Union"

    return type_name


def _get_generic_name(v: Type[Any], origin: Type[Any]) -> str:
    # get generic origin name
    if hasattr(origin, "_name"):  # In python 3.8 Union has _name attribute
        origin_name = origin._name
    elif hasattr(origin, "__name__"):
        origin_name = origin.__name__

    origin_name = type_normalize(origin_name)

    # Annotated is a special case, we need to get the first argument
    if origin_name == "Annotated":
        return _get_name(get_args(v)[0])

    sub_names = [_get_name(sub_type) for sub_type in get_args(v)]

    # Union is another special case, we need to join the sub names with "|"
    if origin_name == "Union":
        return " | ".join(sub_names)

    return f"{origin_name}[{', '.join(sub_names)}]"


def _get_name(v: Type[Any]) -> str:
    """get name from type"""
    if v in base_types:
        return v.__name__

    # Support literal inner parts, like Literal[True, False]
    if type(v) in base_types:
        if isinstance(v, str):
            return f"'{v}'"
        return str(v)

    origin = get_origin(v)
    if origin is None:
        return "..." if v == Ellipsis else type_normalize(v.__name__)  # type: ignore[comparison-overlap]

    return _get_generic_name(v, origin)


def _get_dependencies(v: Type[Any]) -> Set[str]:
    """get dependencies from property types"""
    ans: Set[str] = set()

    if v in base_types:
        return ans

    origin = get_origin(v)

    if origin is None and hasattr(v, "__name__") and v != NoneType:
        ans.add(v.__name__)

    if origin is not None:
        for sub_v in get_args(v):
            ans |= _get_dependencies(sub_v)

    return ans


def get_default_value(field: FieldInfo) -> str:
    default_value = ""
    if field.default_factory is not None:
        default_value = field.default_factory.__name__
    elif not field.is_required():
        if isinstance(field.default, str) and not isinstance(field.annotation, EnumMeta):
            default_value = f"'{field.default}'"
        else:
            default_value = str(field.default)

    return default_value


class PydanticParser:
    """parse pydantic module to mermaid graph"""

    def __call__(self, module: ModuleType) -> MermaidGraph:
        graph = MermaidGraph()

        for class_name, class_type in module.__dict__.items():
            if class_name in ["BaseModel", "Enum", "Extra", "Relations"]:
                continue

            if type(class_type) not in [ModelMetaclass, EnumMeta]:
                continue

            model_type: Type[BaseModel] = class_type
            # inheritance
            parents = model_type.mro()
            first_parent = parents[1]
            parent_name = first_parent.__name__
            graph.child_parents[class_name] = {parent_name}
            if parent_name in graph.class_dict:
                if parent_name not in graph.parent_children:
                    graph.parent_children[parent_name] = set()
                graph.parent_children[parent_name].add(class_name)

            # fields
            annotation = ""
            properties: List[Property] = []
            if isinstance(class_type, ModelMetaclass):
                fields: Dict[str, FieldInfo] = model_type.model_fields
                graph.service_clients[class_name] = set()
                for name, field in fields.items():
                    if field.annotation is None:  # pragma: no cover
                        continue

                    properties.append(
                        Property(name=name, type=_get_name(field.annotation), default_value=get_default_value(field))
                    )
                    # dependencies
                    graph.service_clients[class_name] = graph.service_clients[class_name] | _get_dependencies(
                        field.annotation
                    )

                graph.service_clients[class_name] = graph.service_clients[class_name]
            elif isinstance(class_type, EnumMeta):
                annotation = "Enumeration"
                for name, member in class_type._member_map_.items():
                    field_type = type(member.value).__name__
                    value = f"'{member.value}'" if isinstance(member.value, str) else str(member.value)
                    properties.append(Property(name=name, type=field_type, default_value=value))

            graph.class_dict[class_name] = MermaidClass(name=class_name, properties=properties, annotation=annotation)
            graph.class_names.append(class_name)

        return graph
