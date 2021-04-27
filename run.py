"""This module is the starting point for the program

Raises:
    Exception: Input and program execution exception
Returns:
    RoverPoint: It will print out the calculated rover position in the grid
"""
import re

from src.enums.movementcommand import MovementCommand
from src.grid import Grid
from src.rover import Rover
from src.roverpoint import RoverPoint
from src.enums.orientation import Orientation


def main():
    """This is the main function of the program
       responsible for user input and some validation
    :return:
        a RoverPoint object cast to_string which is printed  for the user
    """
    input_grid_size = input("Please enter the Grid size (Space Separated):")
    # parse initial grid size/grid input
    if not re.match(re.compile("^[0-9]* [0-9]*$"), input_grid_size):
        raise Exception("Invalid grid size/grid dimensions")
    grid_size_list = input_grid_size.split()
    grid = Grid(int(grid_size_list[0]), int(grid_size_list[1]))

    while 1:
        try:
            # get the initial position in the Grid
            initial_pos = input("Please enter the position on the grid:").upper()
            if not re.match(re.compile("^[0-9]* [0-9]* [NSEW]$"), initial_pos):
                raise Exception("Invalid position entered for the rover")

            x_axis, y_axis, direction = initial_pos.split()
            pos = RoverPoint(int(x_axis), int(y_axis), Orientation(direction))
            # get the commands for the rover
            cmd_input = input("Please enter the instruction for the rover:").upper()

            # invoke the corresponding functions passing prev position
            commands = [MovementCommand(command) for command in list(cmd_input.replace('\n', ''))]
            rover = Rover(grid, pos)
            rover.run_commands(commands)

            print(rover.active_position.to_string())
            while True:
                cont_rover = input("Continue instructing the rover (y/n)?").lower()
                if cont_rover in ("yes", "y"):
                    break
                elif cont_rover in ("no", "n"):
                    raise SystemExit
                else:
                    print("Sorry, I didn't understand that.")
        except TypeError as type_error:
            print("An input error took place, ", type_error)
        except ValueError as v_error:
            print("An value input error took place, ", v_error)
        except KeyboardInterrupt:
            print('Caught KeyboardInterrupt')


if __name__ == '__main__':
    main()
