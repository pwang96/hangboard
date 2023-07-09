"""Account manager module"""
import logging

from .user import User


logger = logging.Logger("AccountManager")

class AccountManager:
    """Class for managing accounts"""
    def __init__(self):
        self.users: dict[int, User] = {}
        self.existing_usernames = set()
        self.current_id = 0

    def add_user(self, username: str, email: str, password: str) -> None:
        """Add a user

        This does some validation that the username does not exist already.
        TODO: make sure email is not re-used.
        """
        if username in self.existing_usernames:
            logger.warn(f"{username} already exists")
            raise ValueError(f"{username} already exists in the system")

        user_id = self.current_id
        self.current_id += 1
        logger.info(f"Adding user {username} with {user_id=}")
        new_user = User(user_id, username, email, password)
        self.existing_usernames.add(username)

        self.users[user_id] = new_user


