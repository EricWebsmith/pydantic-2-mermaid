```mermaid
classDiagram
    class Animal {
    }

    class Fish {
        gill: str = 'gill'
    }

    class Beast {
        legs: int
    }

    class Bird {
        wings: int
    }

    class Dog {
    }

    class Cat {
    }

    class Salmon {
    }

    class Eagle {
    }


    Animal <|-- Bird
    Animal <|-- Beast
    Animal <|-- Fish
    Beast <|-- Dog
    Beast <|-- Cat
    Fish <|-- Salmon
    Bird <|-- Eagle
```