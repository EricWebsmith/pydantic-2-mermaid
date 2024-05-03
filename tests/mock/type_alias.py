from typing import Generic, List, TypeVar

from pydantic import BaseModel


class Cat(BaseModel):
    pass


class Dog(BaseModel):
    pass


AnimalT = TypeVar("AnimalT", bound=Cat | Dog)


class Shop(BaseModel, Generic[AnimalT]):
    pets: List[AnimalT]


class PetShopAssociation(BaseModel):
    shops: list[Shop[Dog] | Shop[Cat]]


# TODO: fix generic dependencies like PetShopAssociation ..> Shop[Cat]
