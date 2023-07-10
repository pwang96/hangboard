"""Weight"""
from enum import Enum, auto


class ReferenceWeight(Enum):
    """WeightType enum represents either free weight or body weight as a reference"""

    FREE = auto()
    BODYWEIGHT = auto()


class Weight:
    """Weight class provides information on weights used during hangs"""

    def __init__(self, reference_weight: ReferenceWeight, additional_weight: int):
        self.reference = reference_weight
        self.additional = additional_weight
