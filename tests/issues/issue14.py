from pydantic import BaseModel
from json import JSONDecoder


class Foo(BaseModel, arbitrary_types_allowed=True):

    type_is_out_of_module: JSONDecoder
    """the type of this field is outside of this module"""
