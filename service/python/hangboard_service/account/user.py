"""User module"""
from dataclasses import dataclass


@dataclass
class User:
    """Class representing a user"""
    user_id: int
    username: str
    email: str
    password: str
