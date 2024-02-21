from enum import Enum

from pydantic import BaseModel


class Flavor(str, Enum):
    apple = "apple"
    pumpkin = "pumpkin"
    potato = "potato"


class Pie(BaseModel):
    flavor: Flavor


class ApplePie(Pie):
    flavor: Flavor = Flavor.apple


class PumpkinPie(Pie):
    flavor: Flavor = Flavor.pumpkin
