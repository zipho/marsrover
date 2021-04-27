"""This module is an enum class for the rover object orientation
"""
from enum import Enum


class Orientation(Enum):
    """This class defines the orientations possible for the rover which are the four cardinal directions
    Args:
        Enum (direction): [acronym]
    """
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
