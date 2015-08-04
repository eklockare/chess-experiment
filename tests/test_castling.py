# -*- coding: utf-8 -*-
import copy
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from move_inspect_result import MoveInspectResult, CastlingMoveInspectResult
from pieces.bishop import Bishop
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece
import directions


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
                        CastlingMoveInspectResult(True, False, True, False, h1_rook,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_if_king_has_moved(self):
        e1_king = King(ChessCoord('E', '1'), white)
        e1_king.update_coord(ChessCoord('E', '2'))
        h1_rook = Rook(ChessCoord('H', '1'), white)
        pieces = [e1_king, h1_rook]
        inspect_move_result = e1_king.inspect_move(pieces, ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, False, h1_rook,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_if_king_has_moved_and_moved_back(self):
        e1_king = King(ChessCoord('E', '1'), white)
        e1_king.update_coord(ChessCoord('E', '2'))
        e1_king.update_coord(ChessCoord('E', '1'))
        h1_rook = Rook(ChessCoord('H', '1'), white)
        pieces = [e1_king, h1_rook]
        inspect_move_result = e1_king.inspect_move(pieces, ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, False, h1_rook,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_if_rook_has_moved(self):
        e1_king = King(ChessCoord('E', '1'), white)
        h1_rook = Rook(ChessCoord('H', '1'), white)
        h1_rook.update_coord(ChessCoord('H', '2'))
        pieces = [e1_king, h1_rook]
        inspect_move_result = e1_king.inspect_move(pieces, ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, False, None,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_if_rook_has_moved_and_moved_back(self):
        e1_king = King(ChessCoord('E', '1'), white)
        h1_rook = Rook(ChessCoord('H', '1'), white)
        h1_rook.update_coord(ChessCoord('H', '2'))
        h1_rook.update_coord(ChessCoord('H', '1'))
        pieces = [e1_king, h1_rook]
        inspect_move_result = e1_king.inspect_move(pieces, ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, False, None,
                                                  ChessCoord('F', '1')))

    def test_castling_should_not_be_possible_with_pieces_in_the_way(self):
        all_pieces = copy.deepcopy(starting_pieces)
        a1_rook = select_piece(ChessCoord('A', '1'), all_pieces)
        e1_king = select_piece(ChessCoord('E', '1'), all_pieces)

        inspect_move_result = e1_king.inspect_move(all_pieces,
                                                   ChessCoord('B', '1'))
        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, True, True, False, a1_rook,
                                                  ChessCoord('C', '1')))




    def test_castling_invalid_enemy_piece_attacks_square_in_between(self):
        e1_king = King(ChessCoord('E', '1'), white)
        h1_rook = Rook(ChessCoord('H', '1'), white)
        f5_rook = Rook(ChessCoord('F', '5'), black)
        pieces = [e1_king, h1_rook, f5_rook]
        inspect_move_result = e1_king.inspect_move(pieces,
                                                   ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, True, h1_rook,
                                                  ChessCoord('F', '1')))

    def test_castling_be_possible_for_north_side(self):
        all_pieces = copy.deepcopy(starting_pieces)
        h8_rook = select_piece(ChessCoord('H', '8'), all_pieces)
        e8_king = select_piece(ChessCoord('E', '8'), all_pieces)
        g8_knight = select_piece(ChessCoord('G', '8'), all_pieces)
        f8_bishop = select_piece(ChessCoord('F', '8'), all_pieces)
        g8_knight.update_coord(ChessCoord('H', '6'))
        f8_bishop.update_coord(ChessCoord('D', '6'))

        inspect_move_result = e8_king.inspect_move(all_pieces,
                                                   ChessCoord('G', '8'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(True, False, True, False, h8_rook,
                                                  ChessCoord('F', '8')))

    def test_castling_be_possible_for_north_side_long(self):
        all_pieces = copy.deepcopy(starting_pieces)
        a8_rook = select_piece(ChessCoord('A', '8'), all_pieces)
        e8_king = select_piece(ChessCoord('E', '8'), all_pieces)

        d8_queen = select_piece(ChessCoord('D', '8'), all_pieces)
        b8_knight = select_piece(ChessCoord('B', '8'), all_pieces)
        c8_bishop = select_piece(ChessCoord('C', '8'), all_pieces)
        d8_queen.update_coord(ChessCoord('D', '6'))
        b8_knight.update_coord(ChessCoord('C', '6'))
        c8_bishop.update_coord(ChessCoord('A', '6'))

        inspect_move_result = e8_king.inspect_move(all_pieces,
                                                   ChessCoord('B', '8'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(True, False, True, False, a8_rook,
                                                  ChessCoord('C', '8')))

    def test_castling_not_possible_if_in_check(self):
        e1_king = King(ChessCoord('E', '1'), white)
        h1_rook = Rook(ChessCoord('H', '1'), white)
        e4_rook_black = Rook(ChessCoord('E', '4'), black)
        pieces = [e1_king, h1_rook, e4_rook_black]
        inspect_move_result = e1_king.inspect_move(pieces,
                                                   ChessCoord('G', '1'))

        self.failUnless(inspect_move_result ==
                        CastlingMoveInspectResult(False, False, True, False, h1_rook,
                                                  ChessCoord('F', '1')))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
