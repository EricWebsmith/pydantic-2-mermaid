```mermaid
classDiagram
    class County {
        name: str
        population: int
    }

    class Region {
        name: str
        population: int
        counties: list[County]
    }

    class Province {
        name: str
        population: int
        regions: list[Region]
    }

    class City {
        name: str
        population: int
        counties: list[County]
    }

    class Country {
        name: str
        population: int
        provinces: list[Province]
        cities: list[City]
    }

    Country ..> City
    Country ..> Province
    Province ..> Region
    Region ..> County
    City ..> County

```
