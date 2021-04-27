"""This module defines the class of a Grid object
   when imported, the module makes the Grid class accessible
Returns:
    [class]: [Grid]
"""
from .roverpoint import RoverPoint


class Grid:
    """This class defines the attributes and the methods of a grid object
    """

    def __init__(self, x_axis: int, y_axis: int):
        """Inititialisation function of the grid class

        Args:
            x_axis (int): the max point of x-axis in the grid
            y_axis (int): the max point of y-axis in the grid
        """
        self.out_x_axis: int = x_axis
        self.out_y_axis: int = y_axis

    def is_position_within_grid_area(self, pos: RoverPoint):
        """This method is to validate the RoverPoint object within the Grid object

        Args:
            pos (RoverPoint): the assumed position of the rover object

        Returns:
            [boolean]: true/false is returned by the method
        """
        return not (pos.x_axis > self.out_x_axis or
                    pos.y_axis > self.out_y_axis)
