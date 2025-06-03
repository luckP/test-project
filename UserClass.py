from dataclasses import dataclass


@dataclass
class User:
    """User model class"""
    name: str
    age: int
    is_active: bool
