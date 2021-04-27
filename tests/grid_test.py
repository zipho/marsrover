"""Test module for the Grid class"""
from marsrover.src.grid import Grid
from marsrover.src.roverpoint import RoverPoint


class TestGrid:
    """TestGrid class tests when the rover's position is within a grid area,
       and outside of the grid.
    """

    def test_position_within_grid_area(self):
        """This is to test the position if its within the grid area"""
        # Given
        grid = Grid(3, 3)
        expected_boolean = True  # inside boundary
        # When
        result = grid.is_position_within_grid_area(RoverPoint(1, 2, 'N'))
        assert expected_boolean == result

    def test_position_not_within_grid_area(self):
        """This is to test the position if its not within the grid area"""
        # Given
        grid = Grid(3, 3)
        expected_boolean = False  # outside boundary
        # When
        result = grid.is_position_within_grid_area(RoverPoint(4, 4, 'N'))
        assert expected_boolean == result
