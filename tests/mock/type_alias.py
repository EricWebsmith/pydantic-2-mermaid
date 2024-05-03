from typing import Generic, List, TypeVar, Union

from pydantic import BaseModel


class Cat(BaseModel):
    pass


class Dog(BaseModel):
    pass


AnimalT = TypeVar("AnimalT", bound=Union[Cat, Dog])


class Shop(BaseModel, Generic[AnimalT]):
    pets: List[AnimalT]


class PetShopAssociation(BaseModel):
    shops: List[Union[Shop[Dog], Shop[Cat]]]


# TODO: fix generic dependencies like PetShopAssociation ..> Shop[Cat]
