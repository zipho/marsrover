from marsrover.src.roverpoint import RoverPoint


class Grid:

    def __init__(self, x_axis: int, y_axis: int):
        self.out_x_axis: int = x_axis
        self.out_y_axis: int = y_axis

    def is_position_within_grid_area(self, pos: RoverPoint):
        return not (pos.x_axis > self.out_x_axis or
                    pos.y_axis > self.out_y_axis)
