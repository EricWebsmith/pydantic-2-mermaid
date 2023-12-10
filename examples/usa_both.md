```mermaid
classDiagram
    class AdministrativeDivision {
        name: str
        population: int
    }

    class Municipality {
    }

    class MinorCivilDivision {
    }

    class County {
        municipalities: list[Municipality]
        minor_civil_divisions: list[MinorCivilDivision]
    }

    class CountyEquivalant {
    }

    class State {
        counties: list[County]
        county_equivalants: list[CountyEquivalant]
    }

    class FederalDistrict {
    }

    class InhabitedTerritory {
    }

    class HabitedTerritory {
    }

    class Federal {
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

    AdministrativeDivision <|-- County
    AdministrativeDivision <|-- InhabitedTerritory
    AdministrativeDivision <|-- Municipality
    AdministrativeDivision <|-- FederalDistrict
    AdministrativeDivision <|-- HabitedTerritory
    AdministrativeDivision <|-- State
    AdministrativeDivision <|-- Federal
    AdministrativeDivision <|-- CountyEquivalant
    AdministrativeDivision <|-- MinorCivilDivision
```