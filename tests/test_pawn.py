# -*- coding: utf-8 -*-
import copy
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from directions import go_north, go_south
from move_inspect_result import MoveInspectResult
from pieces.pawn import Pawn
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece


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
        self.white_pawn.update_coord(ChessCoord('D', '3'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('D', '5')).
                    is_valid_move)

    def test_is_invalid_move_two_step_from_start_wrong_direction(self):
        pieces = []
        self.white_pawn.update_coord(ChessCoord('A', '7'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('A', '5')).
                    is_valid_move)

    def test_update_coors_white(self):
        self.white_pawn.update_coord(ChessCoord('A', '3'))
        self.failUnless(self.white_pawn.grid_coord == GridCoord(0, 2))

    def test_update_coors_black(self):
        self.black_pawn.update_coord(ChessCoord('C', '6'))
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
        self.black_pawn.update_coord(ChessCoord('B', '5'))
        self.failIf(self.white_pawn.inspect_move(pieces, ChessCoord('B', '4')).
                    is_valid_move)

    def test_is_valid_move_two_step_from_start_white(self):
        pieces = []
        self.black_pawn.update_coord(ChessCoord('A', '2'))
        self.failUnless(self.white_pawn.inspect_move(pieces, ChessCoord('A', '4')).
                        is_valid_move)

    def test_is_valid_move_two_step_from_start_black(self):
        pieces = []
        self.black_pawn.update_coord(ChessCoord('C', '7'))
        self.failUnless(self.black_pawn.inspect_move(pieces, ChessCoord('C', '5')).
                        is_valid_move)

    def test_inspect_move_taking_enemy(self):
        pieces = [self.white_pawn, self.black_pawn]
        self.white_pawn.update_coord(ChessCoord('B', '6'))
        self.black_pawn.update_coord(ChessCoord('C', '7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('B', '6'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(True, False, [GridCoord(1, 5)],
                                          self.white_pawn))

    def test_inspect_move_blocked_by_friendly_taking(self):
        pieces = [Pawn(ChessCoord('C', '6'), white, go_north), self.white_pawn]
        self.white_pawn.update_coord(ChessCoord('B', '5'))

        move_inspect_result = self.white_pawn.inspect_move(pieces, ChessCoord('C', '6'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [],
                                          pieces[0]))

    def test_inspect_move_blocked_by_enemy(self):
        pieces = [self.white_pawn, self.black_pawn]
        self.white_pawn.update_coord(ChessCoord('B', '2'))
        self.black_pawn.update_coord(ChessCoord('B', '3'))

        move_inspect_result = self.white_pawn.inspect_move(pieces, ChessCoord('B', '3'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(1, 2)],
                                          self.black_pawn))

    def test_inspect_move_blocked_by_friendly(self):
        pieces = [Pawn(ChessCoord('D', '4'), black, go_south), self.black_pawn]
        self.black_pawn.update_coord(ChessCoord('D', '5'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('D', '4'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [GridCoord(3, 3)],
                                          pieces[0]))

    def test_inspect_move_two_steps_blocked_by_friendly(self):
        pieces = [Pawn(ChessCoord('C', '6'), black, go_south), self.black_pawn]
        self.black_pawn.update_coord(ChessCoord('C', '7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('C', '5'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [],
                                          pieces[0]))

    def test_inspect_move_two_steps_blocked_by_enemy(self):
        pieces = [Pawn(ChessCoord('C', '6'), white, go_south), self.black_pawn]
        self.black_pawn.update_coord(ChessCoord('C', '7'))

        move_inspect_result = self.black_pawn.inspect_move(pieces, ChessCoord('C', '5'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [],
                                          pieces[0]))

    def test_en_passant_square_set(self):
        self.black_pawn.update_coord(ChessCoord('C', '7'))
        self.failIf(self.black_pawn.en_passant_square)
        self.black_pawn.update_coord(ChessCoord('C', '5'))
        self.failUnless(self.black_pawn.en_passant_square == GridCoord(2, 5))

    def test_en_passant_can_be_taken(self):
        self.black_pawn.update_coord(ChessCoord('E', '7'))
        self.black_pawn.update_coord(ChessCoord('E', '5'))
        self.failUnless(self.black_pawn.en_passant_square == GridCoord(4, 5))

        pieces = [self.black_pawn, self.white_pawn, Rook(ChessCoord('A', '1'), black)]
        self.white_pawn.update_coord(ChessCoord('F', '5'))

        move_inspect_result = self.white_pawn.inspect_move(pieces, ChessCoord('E', '6'))
        self.failUnless(move_inspect_result ==
                        MoveInspectResult(True, False, [GridCoord(4, 5)], self.black_pawn))

    def test_en_passant_is_removed_when_pawn_is_moved_again(self):
        self.white_pawn.update_coord(ChessCoord('A', '2'))
        self.failIf(self.white_pawn.en_passant_square)

        self.white_pawn.update_coord(ChessCoord('A', '4'))
        self.failUnless(self.white_pawn.en_passant_square == GridCoord(0, 2))

        self.white_pawn.update_coord(ChessCoord('A', '5'))
        self.failIf(self.white_pawn.en_passant_square)

    def test_black_pawn_not_allowed_to_take_pawn_across_board(self):
        all_pieces = copy.deepcopy(starting_pieces)
        g7_pawn = select_piece(ChessCoord('G', '7'), all_pieces)

        inspect_move_result = g7_pawn.inspect_move(all_pieces, ChessCoord('H', '2'))
        self.failIf(inspect_move_result.is_valid_move)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
