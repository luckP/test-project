from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    is_active: bool
