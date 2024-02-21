```mermaid
classDiagram
    class Flavor {
        <<Enumeration>>
        apple: str = 'apple'
        pumpkin: str = 'pumpkin'
        potato: str = 'potato'
    }

    class Pie {
        flavor: Flavor
    }

    class ApplePie {
    }

    class PumpkinPie {
    }


    Pie <|-- ApplePie
    Pie <|-- PumpkinPie
```