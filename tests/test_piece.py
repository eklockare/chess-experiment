# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from directions import go_north, go_south, go_west, go_east, DirectionResult
from pieces.pawn import Pawn
from pieces.piece import Piece
import collections
import util
from movement import MoveResult


class PieceTests(unittest.TestCase):

    def setUp(self):
        self.directions = [go_west]
        self.black_piece = Piece(ChessCoord('H', '6'), black, 'x', 'c', self.directions)

    def test_constructor(self):
        self.failUnless(self.black_piece.letter is 'x')
        self.failUnless(self.black_piece.colour is black)
        self.failUnless(self.black_piece.move_directions == self.directions)
        self.failUnless(self.black_piece.chess_coord == ChessCoord('H', '6'))
        self.failUnless(self.black_piece.grid_coord == GridCoord(7, 5))

    def test_direction_and_squares_valid_move(self):
        move = ChessCoord('C', '6')
        grid_move = board_parts.chess_coord_to_grid_coord(move)
        valid_direction, direction, squares = self. \
            black_piece.get_direction_and_squares(grid_move)
        # should not have changed:
        self.failUnless(self.black_piece.chess_coord == ChessCoord('H', '6'))
        self.failUnless(self.black_piece.grid_coord == GridCoord(7, 5))

        self.failUnless(valid_direction)
        self.failUnless(direction == go_west)
        self.failUnless(util.compare_lists(squares,
                                           [GridCoord(2, 5),
                                            GridCoord(3, 5),
                                            GridCoord(4, 5),
                                            GridCoord(5, 5),
                                            GridCoord(6, 5)]))


    def test_is_valid_move_returns_move_result_no_pieces(self):
        move_result = self.black_piece.is_valid_move([], ChessCoord('F', '6'))

        self.failUnless(move_result == MoveResult(True, DirectionResult([
            GridCoord(6, 5),
            GridCoord(5, 5),
            GridCoord(4, 5),
            GridCoord(3, 5),
            GridCoord(2, 5),
            GridCoord(1, 5),
            GridCoord(0, 5)], None)))



def main():
    unittest.main()


if __name__ == '__main__':
    main()
