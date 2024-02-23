from enum import Enum

from pydantic import BaseModel


class Flavor(str, Enum):
    APPLE = "apple"
    PUMPKIN = "pumpkin"
    POTATO = "potato"


class Pie(BaseModel):
    flavor: Flavor


class ApplePie(Pie):
    flavor: Flavor = Flavor.APPLE


class PumpkinPie(Pie):
    flavor: Flavor = Flavor.PUMPKIN
