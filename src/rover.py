from typing import List

from marsrover.src.grid import Grid
from marsrover.src.roverpoint import RoverPoint
from marsrover.enums.movementcommand import MovementCommand

from marsrover.enums.orientation import Orientation


def get_orientation_index(direction):
    r_pos = 0
    for index, v_object in enumerate(Orientation):
        if v_object.value == str(direction):
            r_pos = index
    return int(r_pos)


def get_orientation_object(orientation_point):
    orientation_object = Orientation
    for index, v_object in enumerate(Orientation):
        if index == orientation_point:
            orientation_object = list(Orientation)[index]
    return orientation_object


class Rover:

    def __init__(self, grid: Grid, pos: RoverPoint):
        if not grid.is_position_within_grid_area(pos):
            raise ValueError('rover initial position out of grid area')
        self.grid: Grid = grid
        self.active_position: RoverPoint = pos

    def run_commands(self, commands: List[MovementCommand]):
        for command in commands:
            if command == MovementCommand.FORWARD:
                self.move_forward()
            if command == MovementCommand.RIGHT:
                self.turn_right()
            if command == MovementCommand.LEFT:
                self.turn_left()

    def turn_right(self):
        """
        Creates the x, y co-ordinates data structure (tuple) and calculates direction (RIGHT) from the current_direction_index
        :return: the x - coordinate position, y - coordinate of and the direction faced by the rover
        """
        # modulus operator to ensure increments from 0 to 4 for (NESW)
        orientation = (get_orientation_index(self.active_position.orientation.value) + 1) % 4
        new_pos = RoverPoint(self.active_position.x_axis,
                             self.active_position.y_axis,
                             get_orientation_object(orientation))
        self.active_position = new_pos
        return new_pos

    def turn_left(self):
        """
        Creates the x, y co-ordinates data structure (tuple) and calculates direction (LEFT) from the current_direction_index
        :return: the x - coordinate position, y - coordinate of and the direction faced by the rover
        """
        orientation = (get_orientation_index(self.active_position.orientation.value) - 1 + 4) % 4
        new_pos = RoverPoint(self.active_position.x_axis,
                             self.active_position.y_axis,
                             get_orientation_object(orientation))
        self.active_position = new_pos
        return new_pos

    def move_forward(self):
        """
        """
        # an array for each direction (NESW - (x, y))
        delta_points = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        orientation_index = get_orientation_index(self.active_position.orientation.value)
        new_pos = RoverPoint(self.active_position.x_axis + delta_points[orientation_index][0],
                             self.active_position.y_axis + delta_points[orientation_index][1],
                             get_orientation_object(orientation_index))

        if not self.grid.is_position_within_grid_area(new_pos):
            raise ValueError('rover cannot be driven out of grid area')
        self.active_position = new_pos
        return self.active_position
