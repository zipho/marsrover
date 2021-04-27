"""This module defines the Rover class and utility functions for the rover object

Raises:
    ValueError: Rover initial position is out of the grid area
    ValueError: Rover cannot be driven out of grid area

Returns:
    Rover: Rover object
"""
from typing import List

from .grid import Grid
from .roverpoint import RoverPoint
from .enums.movementcommand import MovementCommand

from .enums.orientation import Orientation


def get_orientation_index(direction):
    """This function returns the orientation index in the enum

    Args:
        direction (Orientation): the Orientation value

    Returns:
        int: the enum index of the given Orientation object
    """
    r_pos = 0
    for index, v_object in enumerate(Orientation):
        if v_object.value == str(direction):
            r_pos = index
    return int(r_pos)


def get_orientation_object(orientation_point):
    """This function returns the Orientation object

    Args:
        orientation_point (int): The enum index of the Orientation object

    Returns:
        Orientation: An orientation object is returned
    """
    orientation_object = Orientation
    for index, v_object in enumerate(Orientation):
        if index == orientation_point:
            orientation_object = list(Orientation)[index]
    return orientation_object


class Rover:
    """The Rover class defines attributes and methods for the rover object
    """
    def __init__(self, grid: Grid, pos: RoverPoint):
        """This method instantiates the rover object
        Args:
            grid (Grid): the defined grid object based on user input
            pos (RoverPoint): the defined initial/current roverpoint within a grid
        Raises:
            ValueError: Rover initial position out of grid area
        """
        if not grid.is_position_within_grid_area(pos):
            raise ValueError('rover initial position out of grid area')
        self.grid: Grid = grid
        self.active_position: RoverPoint = pos

    def run_commands(self, commands: List[MovementCommand]):
        """This method handles the commands by routing them to right class methods
        Args:
            commands (List[MovementCommand]): the MovementCommand object build on user input
        """
        for command in commands:
            if command == MovementCommand.FORWARD:
                self.move_forward()
            if command == MovementCommand.RIGHT:
                self.turn_right()
            if command == MovementCommand.LEFT:
                self.turn_left()

    def turn_right(self):
        """This method creates the x, y co-ordinates data structure (tuple)
           and calculates direction (RIGHT) from the current_direction_index
        Returns:
            RoverPoint object: x - coordinate position,
            y - coordinate of and the direction faced by the rover
        """
        # modulus operator to ensure increments from 0 to 4 for (NESW)
        orientation = (get_orientation_index(self.active_position.orientation.value) + 1) % 4
        new_pos = RoverPoint(self.active_position.x_axis,
                             self.active_position.y_axis,
                             get_orientation_object(orientation))
        self.active_position = new_pos
        return new_pos

    def turn_left(self):
        """This method creates the x, y co-ordinates data structure (tuple)
           and calculates direction (LEFT) from the current_direction_index
        Returns:
            RoverPoint object: x - coordinate position,
            y - coordinate of and the direction faced by the rover
        """
        orientation = (get_orientation_index(self.active_position.orientation.value) - 1 + 4) % 4
        new_pos = RoverPoint(self.active_position.x_axis,
                             self.active_position.y_axis,
                             get_orientation_object(orientation))
        self.active_position = new_pos
        return new_pos

    def move_forward(self):
        """This method moves the rover from one position to the next in the grid
           this involves calculating using the delta points (mapping the cardinal directions)
        Raises:
            ValueError: Rover can not be driven out of the grid
        Returns:
            RoverPoint object: x - coordinate position,
            y - coordinate of and the direction faced by the rover
        """
        # an array of tuples for each direction (NESW - (x, y))
        delta_points = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        orientation_index = get_orientation_index(self.active_position.orientation.value)
        new_pos = RoverPoint(self.active_position.x_axis + delta_points[orientation_index][0],
                             self.active_position.y_axis + delta_points[orientation_index][1],
                             get_orientation_object(orientation_index))

        if not self.grid.is_position_within_grid_area(new_pos):
            raise ValueError('rover cannot be driven out of grid area')
        self.active_position = new_pos
        return self.active_position
