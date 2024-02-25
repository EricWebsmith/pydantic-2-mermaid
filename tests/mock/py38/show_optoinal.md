```mermaid
classDiagram

    class Person {
        name: Union[str, NoneType] = None
        full_name: str = get_name
        age: Union[int, NoneType] = None
        friends: list[str] = list
        city: str
        addr: str = ''
    }



```