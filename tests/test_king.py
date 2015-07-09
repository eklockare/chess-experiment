# -*- coding: utf-8 -*-
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from move_inspect_result import MoveInspectResult
from pieces.king import King
import util
import directions


class KingTests(unittest.TestCase):
    def setUp(self):
        chess_coord_white = ChessCoord('E', '6')
        self.king_white = King(chess_coord_white, white)
        chess_coord_black = ChessCoord('G', '5')
        self.king_black = King(chess_coord_black, black)

    def test_constructor_white(self):
        self.failUnless(self.king_white.letter == 'K')
        self.failUnless(self.king_white.chess_coord == ChessCoord('E', '6'))
        self.failUnless(self.king_white.grid_coord == GridCoord(4, 5))
        self.failUnless(self.king_white.colour == white)
        self.failUnless(self.king_white.symbol == '♔')
        self.failUnless(util.compare_lists(self.king_white.move_directions,
                                           directions.move_directions_queen()))

    def test_constructor_black(self):
        self.failUnless(self.king_black.letter == 'K')
        self.failUnless(self.king_black.chess_coord == ChessCoord('G', '5'))
        self.failUnless(self.king_black.grid_coord == GridCoord(6, 4))
        self.failUnless(self.king_black.colour == black)
        self.failUnless(self.king_black.symbol == '♚')
        self.failUnless(util.compare_lists(self.king_black.move_directions,
                                           directions.move_directions_queen()))

    def test_white_king_allowed_to_move_north1_east1(self):
        pieces = []

        move_inspect_result = self.king_white.inspect_move(pieces,
                                                           ChessCoord('F', '7'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(True, False, [GridCoord(5, 6)], None))

    def test_white_king_not_allowed_to_move_two_steps(self):
        pieces = []

        move_inspect_result = self.king_white.inspect_move(pieces,
                                                           ChessCoord('E', '4'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, False, [GridCoord(4, 4),
                                                         GridCoord(4, 3)], None))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
