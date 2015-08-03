# -*- coding: utf-8 -*-
import unittest

from board_parts import ChessCoord, black, white
from move_inspect_result import MoveInspectResult
from pieces.bishop import Bishop
from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece
import copy
from detect_check_mate import detect_if_king_is_mate

class TestCheckMate(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_mate_queen(self):
        e8_king = King(ChessCoord('E', '8'), black)
        e7_queen = Queen(ChessCoord('E', '7'), white)
        e5_rook = Rook(ChessCoord('E', '5'), white)
        e1_king = King(ChessCoord('E', '1'), white)
        pieces = [e8_king, e7_queen, e5_rook, e1_king]

        black_mate = detect_if_king_is_mate(black, pieces)
        white_mate = detect_if_king_is_mate(white, pieces)

        self.failUnless(black_mate)
        self.failIf(white_mate)

    def test_check_mate_king_can_take_queen(self):
        e8_king = King(ChessCoord('E', '8'), black)
        e7_queen = Queen(ChessCoord('E', '7'), white)
        e1_king = King(ChessCoord('E', '1'), white)
        pieces = [e8_king, e7_queen, e1_king]

        black_mate = detect_if_king_is_mate(black, pieces)
        white_mate = detect_if_king_is_mate(white, pieces)

        self.failIf(black_mate)
        self.failIf(white_mate)

    def test_check_mate_rook_can_take_queen(self):
        e8_king = King(ChessCoord('E', '8'), black)
        e1_king = King(ChessCoord('E', '1'), white)
        e7_queen = Queen(ChessCoord('E', '7'), white)
        e5_rook = Rook(ChessCoord('E', '5'), white)
        c7_rook = Rook(ChessCoord('C', '7'), black)
        pieces = [e8_king, e7_queen, e5_rook, c7_rook, e1_king]

        black_mate = detect_if_king_is_mate(black, pieces)
        white_mate = detect_if_king_is_mate(white, pieces)

        self.failIf(black_mate)
        self.failIf(white_mate)

    def test_check_mate_move_friendly_to_block(self):
        e8_king = King(ChessCoord('E', '8'), black)
        d7_queen = Queen(ChessCoord('D', '7'), black)
        e1_king = King(ChessCoord('E', '1'), white)
        e6_queen = Queen(ChessCoord('E', '6'), white)
        e5_rook = Rook(ChessCoord('E', '5'), white)
        c7_rook = Rook(ChessCoord('C', '7'), black)
        pieces = [e8_king, e6_queen, e5_rook, c7_rook, e1_king, d7_queen]

        black_mate = detect_if_king_is_mate(black, pieces)
        white_mate = detect_if_king_is_mate(white, pieces)

        self.failIf(black_mate)
        self.failIf(white_mate)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
