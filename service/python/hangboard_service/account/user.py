"""User module"""
from dataclasses import dataclass


@dataclass
class User:
    """Class representing a user"""

    user_id: int
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
