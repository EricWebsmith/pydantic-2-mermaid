```mermaid
classDiagram

    class Cat {
    }

    class Dog {
    }

    class PetShopAssociation {
        shops: list[Shop[Dog] | Shop[Cat]]
    }

    class Shop {
        pets: list[AnimalT]
    }

    Shop ..> AnimalT
    PetShopAssociation ..> Shop[Dog]
    PetShopAssociation ..> Shop[Cat]


```