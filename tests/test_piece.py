# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from directions import go_north, go_south, go_west, go_east, DirectionResult, go_north_east
from pieces.pawn import Pawn
from pieces.piece import Piece
import collections
import util
from movement import MoveInspectResult


class PieceTests(unittest.TestCase):

    def setUp(self):
        self.directions = [go_west, go_east, go_north, go_north_east]
        self.black_piece = Piece(ChessCoord('H', '6'), black, 'P', 'P', self.directions)

        self.other_piece_B4 = Piece(ChessCoord('B', '4'), white, 'P', 'P', self.directions)
        self.other_piece_C6 = Piece(ChessCoord('C', '6'), black, 'P', 'P', self.directions)
        self.other_piece_G3 = Piece(ChessCoord('G', '3'), white, 'P', 'P', self.directions)
        self.other_piece_D7 = Piece(ChessCoord('D', '7'), white, 'P', 'P', self.directions)

        self.some_pieces = [
            Piece(ChessCoord('A', '1'), black, 'P', 'P', self.directions),
            self.other_piece_B4,
            self.other_piece_C6,
            self.other_piece_G3,
            self.other_piece_D7
        ]

    def test_constructor(self):
        self.failUnless(self.black_piece.letter is 'P')
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
        self.failUnless(move_result == MoveInspectResult(True, False, [
            GridCoord(6, 5),
            GridCoord(5, 5)], None))

    def test_is_valid_move_returns_move_result_with_pieces(self):
        move_result = self.black_piece.is_valid_move(self.some_pieces, ChessCoord('F', '6'))
        self.failUnless(move_result == MoveInspectResult(True, False, [
            GridCoord(6, 5),
            GridCoord(5, 5)], None))

    def test_is_invalid_move_returns_move_result_with_own_blocking_piece_end_square(self):
        self.black_piece.update_coords(ChessCoord('A', '4'))
        move_result = self.black_piece.is_valid_move(self.some_pieces, ChessCoord('C', '6'))
        self.failUnless(move_result == MoveInspectResult(False, True, [GridCoord(1, 3)], self.other_piece_B4))

    def test_is_valid_move_returns_move_result_with_enemy_piece_end_square(self):
        self.black_piece.update_coords(ChessCoord('G', '1'))
        move_result = self.black_piece.is_valid_move(self.some_pieces, ChessCoord('G', '3'))

        self.failUnless(move_result == MoveInspectResult(True, False,
            [GridCoord(6, 1), GridCoord(6, 2)],
            self.other_piece_G3)
        )

    def test_is_invalid_move_result_with_enemy_piece_blocking(self):
        self.black_piece.update_coords(ChessCoord('B', '5'))
        move_result = self.black_piece.is_valid_move(self.some_pieces, ChessCoord('E', '8'))
        self.failUnless(move_result == MoveInspectResult(False, True,
            [GridCoord(2, 5)],
            self.other_piece_C6)
        )

    def test_is_invalid_move_result_with_friendly_piece_blocking(self):
        self.black_piece.update_coords(ChessCoord('D', '4'))
        move_result = self.black_piece.is_valid_move(self.some_pieces, ChessCoord('A', '4'))
        self.failUnless(move_result == MoveInspectResult(False, True,
            [GridCoord(2, 3),
             GridCoord(1, 3)],
            self.other_piece_B4)
        )


def main():
    unittest.main()


if __name__ == '__main__':
    main()
