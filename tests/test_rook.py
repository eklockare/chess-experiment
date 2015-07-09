# -*- coding: utf-8 -*-
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from pieces.rook import Rook
import util
import directions


class RookTests(unittest.TestCase):
    def setUp(self):
        chess_coord_white = ChessCoord('F', '8')
        self.rook_white = Rook(chess_coord_white, white)
        chess_coord_black = ChessCoord('E', '3')
        self.rook_black = Rook(chess_coord_black, black)

    def test_constructor_white(self):
        self.failUnless(self.rook_white.letter == 'R')
        self.failUnless(self.rook_white.chess_coord == ChessCoord('F', '8'))
        self.failUnless(self.rook_white.grid_coord == GridCoord(5, 7))
        self.failUnless(self.rook_white.colour == white)
        self.failUnless(self.rook_white.symbol == '♖')
        self.failUnless(util.compare_lists(self.rook_white.move_directions,
                                           directions.move_directions_rook()))

    def test_constructor_black(self):
        self.failUnless(self.rook_black.letter == 'R')
        self.failUnless(self.rook_black.chess_coord == ChessCoord('E', '3'))
        self.failUnless(self.rook_black.grid_coord == GridCoord(4, 2))
        self.failUnless(self.rook_black.colour == black)
        self.failUnless(self.rook_black.symbol == '♜')
        self.failUnless(util.compare_lists(self.rook_black.move_directions,
                                           directions.move_directions_rook()))

    def test_white_rook_allowed_to_move_south7(self):
        pieces = []
        self.failUnless(self.rook_white.inspect_move(pieces,
                                                     ChessCoord('F', '1')).is_valid_move)

    def test_black_rook_allowed_to_move_west4(self):
        pieces = []
        self.failUnless(self.rook_black.inspect_move(pieces,
                                                     ChessCoord('A', '3')).is_valid_move)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
