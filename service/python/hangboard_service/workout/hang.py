"""Hang class"""
import datetime
from enum import Enum, auto

from .weight import Weight


class Hand(Enum):
    """Hand enum"""

    LEFT = auto()
    RIGHT = auto()
    BOTH = auto()


class Hang:
    """Hang class

    A Hang represents one effort. This encodes all metadata about the hang and the effort.
    """

    def __init__(self, hang_start: datetime.datetime, edge: str, hand: Hand, weight: Weight):
        self.hang_start = hang_start
        self.edge = edge
        self.hand = hand
        self.weight = weight
