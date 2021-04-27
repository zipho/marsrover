from marsrover.enums.orientation import Orientation
from marsrover.src.roverpoint import RoverPoint


class TestRoverPoint:

    def test_to_tuple(self):
        # Given
        rover_point = RoverPoint(3, 3, Orientation.NORTH)
        expected_tuple = (3, 3, 'N')
        # When
        result = rover_point.to_tuple()
        assert expected_tuple == result

    def test_to_string(self):
        #Given
        rover_point = RoverPoint(3, 4, Orientation.SOUTH)
        expected_tuple = '3 4 S'
        # When
        result = rover_point.to_string()
        assert expected_tuple == result


