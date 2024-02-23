```mermaid
classDiagram

    class Municipality {
        name: str
        population: int
    }

    class MinorCivilDivision {
        name: str
        population: int
    }

    class County {
        name: str
        population: int
        municipalities: list[Municipality]
        minor_civil_divisions: list[MinorCivilDivision]
    }

    class CountyEquivalant {
        name: str
        population: int
    }

    class State {
        name: str
        population: int
        counties: list[County]
        county_equivalants: list[CountyEquivalant]
    }

    class FederalDistrict {
        name: str
        population: int
    }

    class InhabitedTerritory {
        name: str
        population: int
    }

    class HabitedTerritory {
        name: str
        population: int
    }

    class Federal {
        name: str
        population: int
        federal_distric: FederalDistrict
        states: list[State]
        Inhabited_territories: list[InhabitedTerritory]
        Habited_territories: list[HabitedTerritory]
    }


    County ..> Municipality
    County ..> MinorCivilDivision
    State ..> CountyEquivalant
    State ..> County
    Federal ..> State
    Federal ..> HabitedTerritory
    Federal ..> FederalDistrict
    Federal ..> InhabitedTerritory

```