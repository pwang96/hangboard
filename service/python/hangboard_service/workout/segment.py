"""Segment"""


class SegmentConfiguration:
    """Segment configuration

    Segment configurations specify the parameters of an effort.
    A segment configuration is simply a list of hangs with some specified rest
    between hangs and between hang sets.
    """

    def __init__(self, cycle_time_sec: int):
        self.hangs = []
        self.rest_between_hangs_sec = []  # length len(self.hangs) - 1
        self.cycle_time_sec = cycle_time_sec  # All hangs make one cycle; cycles repeat on this cadence.


class Segment:
    """Segment class

    A segment of a workout is a grouping of a efforts with one configuration.
    """
    def __init__(self, config: SegmentConfiguration):
        self.config = config