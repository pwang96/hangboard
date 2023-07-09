"""Workout session"""
import datetime


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

    def add_segment(self, segment: Segment) -> None:
        """Add a workout segment"""