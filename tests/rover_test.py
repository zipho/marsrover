from src.rover import Rover
from marsrover.roverpoint import RoverPoint
from marsrover.orientation import Orientation
from marsrover.grid import Grid
from marsrover.movementcommand import MovementCommand

import pytest


class TestRover:

    def test_rover_can_move_to_forward(self):
        # Given
        initial_position = RoverPoint(2, 2, Orientation.NORTH)
        grid = Grid(5, 5)
        commands = [MovementCommand.FORWARD,
                    MovementCommand.RIGHT,
                    MovementCommand.FORWARD,
                    MovementCommand.LEFT,
                    MovementCommand.FORWARD]
        rover = Rover(grid, initial_position)
        # When
        rover.processCommands(commands)
        # Then
        expected_final_point = '3 4 N'
        assert rover.currentPosition.toString() == expected_final_point

    def test_cannot_create_rover_if_initial_position_out_of_grid_area(self):
        # Given
        grid = Grid(5, 5)
        initial_position = RoverPoint(6, 5, Orientation.NORTH)
        # Then
        with pytest.raises(ValueError, match='rover initial position out of grid area'):
            rover = Rover(grid, initial_position)

    def test_cannot_move_rover_out_of_grid(self):
        # Given
        initial_position = RoverPoint(2, 2, Orientation.NORTH)
        grid = Grid(3, 3)
        commands = [MovementCommand.FORWARD, MovementCommand.FORWARD, MovementCommand.FORWARD]
        rover = Rover(grid, initial_position)
        # Then
        with pytest.raises(ValueError, match='rover cannot be driven out of grid area'):
            rover.processCommands(commands)
        assert rover.currentPosition.toString() == RoverPoint(2, 3, Orientation.NORTH).toString()