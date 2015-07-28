# -*- coding: utf-8 -*-
import copy
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from move_inspect_result import MoveInspectResult, CastlingMoveInspectResult
from pieces.bishop import Bishop
from pieces.king import King
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece
import directions

# self.pieces = copy.deepcopy(starting_pieces)
class BishopTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_castling_should_be_possible_for_white_king_h1_rook(self):
        e1_king = King(ChessCoord('E', '1'), white)
        h1_rook = Rook(ChessCoord('H', '1'), white)
        pieces = [e1_king, h1_rook]
        inspect_move_result = e1_king.inspect_move(pieces,
                                                        ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(True, False, True, h1_rook,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_with_pieces_in_the_way(self):
        all_pieces = copy.deepcopy(starting_pieces)
        a1_rook = select_piece(ChessCoord('A', '1'), all_pieces)
        e1_king = select_piece(ChessCoord('E', '1'), all_pieces)

        inspect_move_result = e1_king.inspect_move(all_pieces ,
                                                        ChessCoord('B', '1'))
        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, True, True, a1_rook,
                                                  ChessCoord('C', '1')))

    def test_castling_be_possible_for_north_side(self):
        all_pieces = copy.deepcopy(starting_pieces)
        h8_rook = select_piece(ChessCoord('H', '8'), all_pieces)
        e8_king = select_piece(ChessCoord('E', '8'), all_pieces)
        g8_knight = select_piece(ChessCoord('G', '8'), all_pieces)
        f8_bishop = select_piece(ChessCoord('F', '8'), all_pieces)
        g8_knight.update_coords(ChessCoord('H', '6'))
        f8_bishop.update_coords(ChessCoord('D', '6'))

        inspect_move_result = e8_king.inspect_move(all_pieces ,
                                                   ChessCoord('G', '8'))
        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(True, False, True, h8_rook,
                                                  ChessCoord('F', '8')))

    def test_castling_be_possible_for_north_side_long(self):
        all_pieces = copy.deepcopy(starting_pieces)
        a8_rook = select_piece(ChessCoord('A', '8'), all_pieces)
        e8_king = select_piece(ChessCoord('E', '8'), all_pieces)

        d8_queen = select_piece(ChessCoord('D', '8'), all_pieces)
        b8_knight = select_piece(ChessCoord('B', '8'), all_pieces)
        c8_bishop = select_piece(ChessCoord('C', '8'), all_pieces)
        d8_queen.update_coords(ChessCoord('D', '6'))
        b8_knight.update_coords(ChessCoord('C', '6'))
        c8_bishop.update_coords(ChessCoord('A', '6'))

        inspect_move_result = e8_king.inspect_move(all_pieces,
                                                   ChessCoord('B', '8'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(True, False, True, a8_rook,
                                                  ChessCoord('C', '8')))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
