# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from pieces.bishop import Bishop
import util
import directions


class BishopTests(unittest.TestCase):
    def setUp(self):
        chess_coord_white = ChessCoord('F', '8')
        self.bishop_white = Bishop(chess_coord_white, white)
        chess_coord_black = ChessCoord('E', '3')
        self.bishop_black = Bishop(chess_coord_black, black)

    def test_constructor_white(self):
        self.failUnless(self.bishop_white.letter == 'B')
        self.failUnless(self.bishop_white.chess_coord == ChessCoord('F', '8'))
        self.failUnless(self.bishop_white.grid_coord == GridCoord(5, 7))
        self.failUnless(self.bishop_white.colour == white)
        self.failUnless(self.bishop_white.symbol == '♗')
        self.failUnless(util.compare_lists(self.bishop_white.move_directions,
                                           directions.move_directions_bishop()))

    def test_constructor_black(self):
        self.failUnless(self.bishop_black.letter == 'B')
        self.failUnless(self.bishop_black.chess_coord == ChessCoord('E', '3'))
        self.failUnless(self.bishop_black.grid_coord == GridCoord(4, 2))
        self.failUnless(self.bishop_black.colour == black)
        self.failUnless(self.bishop_black.symbol == '♝')
        self.failUnless(util.compare_lists(self.bishop_black.move_directions,
                                           directions.move_directions_bishop()))

    def test_white_bishop_allowed_to_move_south3_west3(self):
        pieces = []
        self.failUnless(self.bishop_white.is_valid_move(pieces,
                                                        ChessCoord('C', '5')).is_valid_move)

    def test_black_bishop_allowed_to_move_north4_west4(self):
            pieces = []
            self.failUnless(self.bishop_black.is_valid_move(pieces,
                                                            ChessCoord('A', '7')).is_valid_move)
def main():
    unittest.main()


if __name__ == '__main__':
    main()
