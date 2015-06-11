# -*- coding: utf-8 -*-
import unittest

import test
import board_parts
from board_parts import GridCoord, ChessCoord, black, white
from directions import go_north, go_south
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
        self.white_pawn.update_coords(ChessCoord('B', '7'))
        self.failIf(self.white_pawn.is_valid_move(pieces, ChessCoord('B', '5')))

    def test_update_coors_white(self):
        self.white_pawn.update_coords(ChessCoord('A', '3'))
        self.failUnless(self.white_pawn.grid_coord == GridCoord(0, 2))

    def test_update_coors_black(self):
        self.black_pawn.update_coords(ChessCoord('C', '6'))
        self.failUnless(self.black_pawn.grid_coord == GridCoord(2, 5))

    def test_is_valid_move_one_step_black(self):
        pieces = []
        self.failUnless(self.black_pawn.is_valid_move(pieces, ChessCoord('B', '6')))

    def test_is_valid_move_one_step_white(self):
        pieces = []
        self.failUnless(self.white_pawn.is_valid_move(pieces, ChessCoord('A', '3')))

    def test_is_invalid_move_backwards(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('B', '5'))
        self.failIf(self.white_pawn.is_valid_move(pieces, ChessCoord('B', '4')))

    def test_is_valid_move_two_step_from_start_white(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('A', '2'))
        self.failUnless(self.white_pawn.is_valid_move(pieces, ChessCoord('A', '4')))

    def test_is_valid_move_two_step_from_start_black(self):
        pieces = []
        self.black_pawn.update_coords(ChessCoord('C', '7'))
        self.failUnless(self.black_pawn.is_valid_move(pieces, ChessCoord('C', '5')))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
