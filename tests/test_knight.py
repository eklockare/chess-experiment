# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from pieces.knight import Knight
import util
import directions


class KnightTests(unittest.TestCase):

    def setUp(self):
        chess_coord_white = ChessCoord('C', '2')
        self.knight_white = Knight(chess_coord_white, white)
        chess_coord_black = ChessCoord('F', '5')
        self.knight_black = Knight(chess_coord_black, black)

    def test_constructor_white(self):
        self.failUnless(self.knight_white.letter == 'Kn')
        self.failUnless(self.knight_white.chess_coord == ChessCoord('C', '2'))
        self.failUnless(self.knight_white.grid_coord == GridCoord(2, 1))
        self.failUnless(self.knight_white.colour == white)
        self.failUnless(self.knight_white.symbol == '♘')
        self.failUnless(util.compare_lists(self.knight_white.move_directions,
                                           directions.move_directions_knight()))

    def test_constructor_black(self):
        self.failUnless(self.knight_black.letter == 'Kn')
        self.failUnless(self.knight_black.chess_coord == ChessCoord('F', '5'))
        self.failUnless(self.knight_black.grid_coord == GridCoord(5, 4))
        self.failUnless(self.knight_black.colour == black)
        self.failUnless(self.knight_black.symbol == '♞')
        self.failUnless(util.compare_lists(self.knight_black.move_directions,
                                           directions.move_directions_knight()))

    def test_white_knight_can_move_north2_east1(self):
        pieces = []
        self.failUnless(self.knight_white.is_valid_move(pieces,
                                                        ChessCoord('D', '4')).is_valid_move)

    def test_white_knight_can_move_south1_east2(self):
        pieces = []
        self.failUnless(self.knight_white.is_valid_move(pieces,
                                                        ChessCoord('A', '1')).is_valid_move)

    def test_white_knight_should_not_be_allowed_invalid_move(self):
        pieces = []
        self.failIf(self.knight_white.is_valid_move(pieces,
                                                        ChessCoord('A', '2')).is_valid_move)

    def test_white_knight_should_not_change_coordinates_after_valid_move_check(self):
            pieces = []
            self.failUnless(self.knight_white.is_valid_move(pieces,
                                                            ChessCoord('D', '4')).is_valid_move)

    def test_white_knight_should_move_when_coordinates_updated(self):
        self.knight_white.update_coords(ChessCoord('D', '6'))
        self.failUnless(self.knight_white.chess_coord == ChessCoord('D', '6'))

    def test_white_knight_should_not_be_allowed_invalid_move_after_update(self):
        pieces = []
        self.knight_white.update_coords(ChessCoord('D', '6'))
        self.failIf(self.knight_white.is_valid_move(pieces,
                                                        ChessCoord('A', '2')).is_valid_move)
        self.failUnless(self.knight_white.chess_coord == ChessCoord('D', '6'))

def main():
    unittest.main()

if __name__ == '__main__':
    main()