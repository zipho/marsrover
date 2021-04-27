"""This module defines the RoverPoint class which helps define the position of the rover in the grid

Returns:
    RoverPoint: A RoverPoint object
"""
from typing import Tuple

from .enums.orientation import Orientation


class RoverPoint:
    """This class defines the methods and attributes of the RoverPoint
       (a position of the rover in a grid)
    """

    def __init__(self, x_coordinates: int, y_coordinates: int, orientation: Orientation):
        """This method instantiates the RoverPoint object
        Args:
            x_coordinates (int): the x-axis value
            y_coordinates (int): the y-axis value
            orientation (Orientation): The direction/orientation of the rover
        """
        self.x_axis: int = x_coordinates
        self.y_axis: int = y_coordinates
        self.orientation: Orientation = orientation

    def to_tuple(self) -> Tuple[int, int, Orientation]:
        """This method return the RoverPoint object in a tuple
        """
        return self.x_axis, self.y_axis, self.orientation.value

    def to_string(self) -> str:
        """This method return the RoverPoint object in a string
        """
        return str(self.x_axis) + " " + str(self.y_axis) + " " + self.orientation.value
