"""Hang class"""
import datetime
from enum import Enum, auto
from typing import Optional

from .weight import Weight


class Hand(Enum):
    """Hand enum"""

    LEFT = auto()
    RIGHT = auto()
    BOTH = auto()


class Edge(Enum):
    """Edge enum"""

    BEASTMAKER_2000_20mm = auto()

    TENSION_BLOCK_20mm = auto()
    TENSION_BLOCK_10mm = auto()
    TENSION_BLOCK_8mm = auto()
    TENSION_BLOCK_6mm = auto()


class Hang:
    """Hang class

    A Hang represents one effort. This encodes all metadata about the hang and the effort.
    """

    def __init__(self, hang_start: datetime.datetime, edge: Edge, hand: Hand, weight: Weight, hangtime: int, notes: Optional[str] = None):
        """Initializer

        Args:
            hang_start (datetime.datetime): The datetime (UTC) the hang was started
            edge (Edge): The edge the hang is on
            hand (Hand): Which hand did the hang
            weight (Weight): The weight of the hang
            hangtime (int): Number of seconds of hang time
            notes (Optional[str], optional): Notes about the hang. Defaults to None.
        """
        self.hang_start = hang_start
        self.edge = edge
        self.hand = hand
        self.weight = weight
        self.hangtime = hangtime
