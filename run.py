import re

from marsrover.enums.movementcommand import MovementCommand
from marsrover.grid import Grid
from marsrover.rover import Rover
from marsrover.roverpoint import RoverPoint
from marsrover.enums.orientation import Orientation


def main():
    input_grid_size = input("Please enter the Grid size (Space Separated):")
    # parse initial grid size/grid input
    if not re.match(re.compile("^[0-9]* [0-9]*$"), input_grid_size):
        raise Exception("Invalid grid size/grid dimensions")
    grid_size_list = input_grid_size.split()
    grid = Grid(int(grid_size_list[0]), int(grid_size_list[1]))

    while 1:
        # get the initial position in the Grid
        initial_pos = input("Please enter the position on the grid:").upper()
        if not re.match(re.compile("^[0-9]* [0-9]* [NSEW]$"), initial_pos):
            raise Exception("Invalid position entered for the rover")
        x_axis, y_axis, direction = initial_pos.split()
        pos = RoverPoint(int(x_axis), int(y_axis), Orientation(direction))

        # get and parse the instructions
        cmd_input = input("Please enter the instruction for the rover:").upper()

        # parse the instructions

        # invoke the corresponding functions passing prev position
        commands = [MovementCommand(command) for command in list(cmd_input.replace('\n', ''))]
        try:
            rover = Rover(grid, pos)
            rover.run_commands(commands)
            print(rover.active_position.to_string())
        except ValueError as error:
            print(error)


if __name__ == '__main__':
    main()
