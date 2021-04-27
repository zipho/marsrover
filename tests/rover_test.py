from marsrover.src.rover import Rover
from marsrover.src.roverpoint import RoverPoint
from marsrover.enums.orientation import Orientation
from marsrover.src.grid import Grid
from marsrover.enums.movementcommand import MovementCommand

import pytest


class TestRover:

    def test_rover_can_move_to_forward(self):
        # Given
        initial_position = RoverPoint(1, 2, Orientation.NORTH)
        grid = Grid(5, 5)
        commands = [MovementCommand.LEFT,
                    MovementCommand.FORWARD,
                    MovementCommand.LEFT,
                    MovementCommand.FORWARD,
                    MovementCommand.LEFT,
                    MovementCommand.FORWARD,
                    MovementCommand.LEFT,
                    MovementCommand.FORWARD,
                    MovementCommand.FORWARD]
        rover = Rover(grid, initial_position)
        # When
        rover.run_commands(commands)
        # Then
        expected_final_point = '1 3 N'
        assert rover.active_position.to_string() == expected_final_point

    def test_cannot_move_rover_out_of_grid(self):
        # Given
        initial_position = RoverPoint(4, 4, Orientation.NORTH)
        grid = Grid(5, 5)
        commands = [MovementCommand.FORWARD, MovementCommand.FORWARD, MovementCommand.FORWARD]
        rover = Rover(grid, initial_position)
        # Then
        with pytest.raises(ValueError, match='rover cannot be driven out of grid area'):
            rover.run_commands(commands)
        assert rover.active_position.to_string() == RoverPoint(4, 5, Orientation.NORTH).to_string()

    def test_cannot_create_rover_if_initial_position_out_of_grid_area(self):
        # Given
        grid = Grid(7, 7)
        initial_position = RoverPoint(8, 7, Orientation.NORTH)
        # Then
        with pytest.raises(ValueError, match='rover initial position out of grid area'):
            rover = Rover(grid, initial_position)
