"""Database utilities"""
from collections import defaultdict
from typing import Any


class InMemoryDB:
    """In memory database"""
    def __init__(self):
        self.tables = defaultdict(lambda: defaultdict())

    def insert(table: str, key: str, value: Any) -> None:
        """Insert the key/value pair into the table"""
        self.tables[table][key] = value

    def get(table: str, key: str) -> Any:
        """Get the key from the table"""
        if table not in self.tables:
            raise RuntimeError(f"No table {table}")
        if key not in self.tables[table]:
            raise RuntimeError(f"No key {key} in {table}")
        return self.tables[table][key]

