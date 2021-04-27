from typing import Tuple

from marsrover.enums.orientation import Orientation


class RoverPoint:

    def __init__(self, x_coordinates: int, y_coordinates: int, orientation: Orientation):
        self.x_axis: int = x_coordinates
        self.y_axis: int = y_coordinates
        self.orientation: Orientation = orientation

    def to_tuple(self) -> Tuple[int, int, Orientation]:
        return self.x_axis, self.y_axis, self.orientation.value

    def to_string(self) -> str:
        return str(self.x_axis) + " " + str(self.y_axis) + " " + self.orientation.value
