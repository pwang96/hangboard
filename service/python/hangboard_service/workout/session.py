"""Workout session"""
import datetime

from .segment import Segment


class Session:
    """Session class

    A session is a fully contained unit of workout. Each session consists of
    one or more workout segments.
    """

    def __init__(self, start: datetime.datetime):
        """Initializer

        Args:
            start (datetime.datetime): Start time of the session
        """
        self.segments = []
        self.start = start

    def add_segment(self, segment: Segment) -> None:
        """Add a workout segment"""
        self.segments.append(segment)
