from typing import Annotated

from pydantic import BaseModel, Field


class AnotatedExample(BaseModel):
    int_prop: Annotated[int, Field(ge=0, le=100)]
    dict_prop: dict[str, Annotated[float, Field(ge=0.1, le=1.0)]] = Field(
        description="Axis stiffness factors", default_factory=dict
    )
