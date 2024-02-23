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
        flavor: Flavor = 'Flavor.apple'
    }

    class PumpkinPie {
        flavor: Flavor = 'Flavor.pumpkin'
    }


    Pie <|-- PumpkinPie
    Pie <|-- ApplePie

```