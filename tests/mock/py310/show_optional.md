```mermaid
classDiagram

    class OldPerson {
        name: Optional[str] = None
        full_name: str = get_name
        age: Optional[int] = None
        friends: list[str] = list
        city: str
        addr: str = ''
    }

    class NewPerson {
        name: UnionType[str, NoneType] = None
        full_name: str = get_name
        age: UnionType[int, NoneType] = None
        friends: list[str] = list
        city: str
        addr: str = ''
    }



```