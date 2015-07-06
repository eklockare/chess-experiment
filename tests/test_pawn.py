# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from directions import go_north, go_south
from movement import MoveInspectResult
from pieces.pawn import Pawn
from pieces.piece import Piece


class PawnTests(unittest.TestCase):

    def setUp(self):
        black_chess_coord = ChessCoord('B', '7')
        white_chess_coord = ChessCoord('A', '2')
        black_colour = black
        white_colour = white
        north_direction = go_north
        south_direction = go_south
        self.black_pawn = Pawn(black_chess_coord, black_colour, south_direction)
        self.white_pawn = Pawn(white_chess_coord, white_colour, north_direction)

    def test_constructor_black(self):
        self.failUnless(self.black_pawn.letter is 'P')
        self.failUnless(self.black_pawn.colour is black)
        self.failUnless(self.black_pawn.move_directions == [go_south])
        self.failUnless(self.black_pawn.chess_coord == ChessCoord('B', '7'))
        self.failUnless(self.black_pawn.grid_coord == GridCoord(1, 6))

    def test_constructor_white(self):
        self.failUnless(self.white_pawn.letter is 'P')
        self.failUnless(self.white_pawn.colour is white)
        self.failUnless(self.white_pawn.move_directions == [go_north])
        self.failUnless(self.white_pawn.chess_coord == ChessCoord('A', '2'))
        self.failUnless(self.white_pawn.grid_coord == GridCoord(0, 1))

    def test_is_invalid_move_two_step_from_not_start(self):
        pieces = []
        self.white_pawn.update_coords(ChessCoord('D', '3'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('D', '5')).
                    is_valid_move)

    def test_is_invalid_move_two_step_from_start_wrong_direction(self):
        pieces = []
        self.white_pawn.update_coords(ChessCoord('A', '7'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('A', '5')).
                    is_valid_move)

    def test_update_coors_white(self):
        self.white_pawn.update_coords(ChessCoord('A', '3'))
        self.failUnless(self.white_pawn.grid_coord == GridCoord(0, 2))

    def test_update_coors_black(self):
        self.black_pawn.update_coords(ChessCoord('C', '6'))
        self.failUnless(self.black_pawn.grid_coord == GridCoord(2, 5))

    def test_is_valid_move_one_step_black(self):
        pieces = []
        self.failUnless(self.black_pawn.inspect_move(pieces, ChessCoord('B', '6')).
                        is_valid_move)

    def test_is_valid_move_one_step_white(self):
        pieces = []
        self.failUnless(self.white_pawn.inspect_move(pieces, ChessCoord('A', '3')).
                        is_valid_move)

    def test_is_invalid_move_backwards(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('B', '5'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('B', '4')).
                    is_valid_move)

    def test_is_valid_move_two_step_from_start_white(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('A', '2'))
        self.failUnless(self.white_pawn.inspect_move(pieces, ChessCoord('A', '4')).
                        is_valid_move)

    def test_is_valid_move_two_step_from_start_black(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('C', '7'))
        self.failUnless(self.black_pawn.inspect_move(pieces, ChessCoord('C', '5')).
                        is_valid_move)

    def test_inspect_move_taking_enemy(self):
        pieces = [self.white_pawn, self.black_pawn]
        self.white_pawn.update_coords(ChessCoord('B','6'))
        self.black_pawn.update_coords(ChessCoord('C', '7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('B', '6'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(True, False, [GridCoord(1, 5)],
                                          self.white_pawn))

    def test_inspect_move_blocked_by_friendly_taking(self):
        pieces = [Pawn(ChessCoord('C', '6'), white, [go_north]), self.white_pawn]
        self.white_pawn.update_coords(ChessCoord('B','5'))

        move_inspect_result = self.white_pawn.inspect_move(pieces, ChessCoord('C', '6'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(2, 5)],
                                          pieces[0]))

    def test_inspect_move_blocked_by_enemy(self):
        pieces = [self.white_pawn, self.black_pawn]
        self.white_pawn.update_coords(ChessCoord('B','2'))
        self.black_pawn.update_coords(ChessCoord('B','3'))

        move_inspect_result = self.white_pawn.inspect_move(pieces, ChessCoord('B', '3'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(1, 2)],
                                          self.black_pawn))

    def test_inspect_move_blocked_by_friendly(self):
        pieces = [Pawn(ChessCoord('D', '4'), black, [go_south]), self.black_pawn]
        self.black_pawn.update_coords(ChessCoord('D','5'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('D', '4'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(3, 3)],
                                          pieces[0]))

    def test_inspect_move_two_steps_blocked_by_friendly(self):
        pieces = [Pawn(ChessCoord('C', '6'), black, [go_south]), self.black_pawn]
        self.black_pawn.update_coords(ChessCoord('C','7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('C', '5'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(2, 5)],
                                          pieces[0]))

    def test_inspect_move_two_steps_blocked_by_enemy(self):
        pieces = [Pawn(ChessCoord('C', '6'), white, [go_south]), self.black_pawn]
        self.black_pawn.update_coords(ChessCoord('C','7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('C', '5'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(2, 5)],
                                          pieces[0]))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
