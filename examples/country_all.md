```mermaid
classDiagram
    class Place {
        name: str
        population: int
    }

    class County {
    }

    class Region {
        counties: list[County]
    }

    class Province {
        regions: list[Region]
    }

    class City {
        counties: list[County]
    }

    class Country {
        provinces: list[Province]
        cities: list[City]
    }


    Region ..> County
    Province ..> Region
    City ..> County
    Country ..> City
    Country ..> Province

    Place <|-- County
    Place <|-- Province
    Place <|-- Region
    Place <|-- City
    Place <|-- Country
```