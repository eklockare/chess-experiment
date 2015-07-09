# -*- coding: utf-8 -*-
import unittest

import directions
from board_parts import GridCoord


class UtilTests(unittest.TestCase):

    def test_get_direction_north(self):
        from_coord = GridCoord(0, 0)
        to_coord = GridCoord(0, 2)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_north)

    def test_get_direction_south(self):
        from_coord = GridCoord(3, 3)
        to_coord = GridCoord(3, 1)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_south)

    def test_get_direction_west(self):
        from_coord = GridCoord(6, 4)
        to_coord = GridCoord(2, 4)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_west)

    def test_get_direction_east(self):
        from_coord = GridCoord(4, 5)
        to_coord = GridCoord(7, 5)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_east)

    def test_get_direction_north_east(self):
        from_coord = GridCoord(4, 4)
        to_coord = GridCoord(6, 6)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_north_east)

    def test_get_direction_north_west(self):
        from_coord = GridCoord(5, 5)
        to_coord = GridCoord(3, 7)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_north_west)

    def test_get_direction_south_west(self):
        from_coord = GridCoord(2, 3)
        to_coord = GridCoord(1, 2)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_south_west)

    def test_get_direction_south_east(self):
        from_coord = GridCoord(2, 4)
        to_coord = GridCoord(4, 0)
        result = directions.get_direction(from_coord, to_coord)
        self.failUnless(result == directions.go_south_east)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
