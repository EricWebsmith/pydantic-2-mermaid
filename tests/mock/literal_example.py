from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class Pie(BaseModel):
    flavor: Literal["apple", "pumpkin"]
    good: Literal[True, False, "Unknown"]
    created: datetime


class ApplePie(Pie):
    flavor: Literal["apple"]


class PumpkinPie(Pie):
    flavor: Literal["pumpkin"]
