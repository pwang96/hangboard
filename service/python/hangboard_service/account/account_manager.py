"""Account manager module"""
import logging
from multiprocessing import Value

from .user import User


logger = logging.Logger("AccountManager")

class AccountManager:
    """Class for managing accounts"""
    def __init__(self):
        self.users: dict[int, User] = {}
        self.username_to_id: dict[str, int] = {}
        self.current_id = 0

    def add_user(self, username: str, first_name: str, last_name: str, email: str, password: str) -> None:
        """Add a user

        This does some validation that the username does not exist already.
        TODO: make sure email is not re-used.
        """
        if username in self.username_to_id:
            logger.warn(f"{username} already exists")
            raise ValueError(f"{username} already exists in the system")

        user_id = self.current_id
        self.current_id += 1
        logger.info(f"Adding user {username} with {user_id=}")
        new_user = User(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        self.username_to_id[username] = user_id

        self.users[user_id] = new_user

    def login(self, username: str, password: str) -> bool:
        """Validate that a username/password combination is valid"""
        user_id = self.username_to_id.get(username, None)
        if user_id is None:
            raise ValueError(f"{username} does not exist in the system")

        user = self.users[user_id]
        return password == user.password
