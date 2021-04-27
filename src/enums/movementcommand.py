"""This module is an enum class for the movements of the rover object
"""
from enum import Enum


class MovementCommand(Enum):
    """These are movements the rover can make on the grid
       additional movements in future can be added to the list
    Args:
        Enum ([movement]): [acronym]
    """
    LEFT = 'L'
    RIGHT = 'R'
    FORWARD = 'M'
