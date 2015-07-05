# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from pieces.queen import Queen
import util
import directions


class QueenTests(unittest.TestCase):
    def setUp(self):
        chess_coord_white = ChessCoord('C', '2')
        self.queen_white = Queen(chess_coord_white, white)
        chess_coord_black = ChessCoord('F', '5')
        self.queen_black = Queen(chess_coord_black, black)

    def test_constructor_white(self):
        self.failUnless(self.queen_white.letter == 'Q')
        self.failUnless(self.queen_white.chess_coord == ChessCoord('C', '2'))
        self.failUnless(self.queen_white.grid_coord == GridCoord(2, 1))
        self.failUnless(self.queen_white.colour == white)
        self.failUnless(self.queen_white.symbol == '♕')
        self.failUnless(util.compare_lists(self.queen_white.move_directions,
                                           directions.move_directions_queen()))

    def test_constructor_black(self):
        self.failUnless(self.queen_black.letter == 'Q')
        self.failUnless(self.queen_black.chess_coord == ChessCoord('F', '5'))
        self.failUnless(self.queen_black.grid_coord == GridCoord(5, 4))
        self.failUnless(self.queen_black.colour == black)
        self.failUnless(self.queen_black.symbol == '♛')
        self.failUnless(util.compare_lists(self.queen_black.move_directions,
                                           directions.move_directions_queen()))

    def test_white_queen_allowed_to_move_north2(self):
        pieces = []
        self.failUnless(self.queen_white.inspect_move(pieces,
                                                       ChessCoord('C', '4')).is_valid_move)

    def test_white_queen_should_not_be_allowed_move_north2_east1(self):
        pieces = []
        self.failIf(self.queen_white.inspect_move(pieces,
                                                   ChessCoord('D', '4')).is_valid_move)

    def test_white_queen_allowed_to_move_north3_east3(self):
        pieces = []
        self.failUnless(self.queen_white.inspect_move(pieces,
                                                       ChessCoord('F', '5')).is_valid_move)

    def test_white_queen_allowed_to_move_south1_west1(self):
        pieces = []
        self.failUnless(self.queen_white.inspect_move(pieces,
                                                       ChessCoord('B', '1')).is_valid_move)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
