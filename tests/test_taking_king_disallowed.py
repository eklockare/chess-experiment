# -*- coding: utf-8 -*-
import copy
import unittest

from board_parts import GridCoord, ChessCoord, black, white
from move_inspect_result import MoveInspectResult, CastlingMoveInspectResult
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece
import directions


class BishopTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_taking_king_not_allowed(self):
        d4_bishop = Bishop(ChessCoord('D', '4'), black)
        e3_king = King(ChessCoord('E', '3'), white)
        pieces = [d4_bishop, e3_king]
        move_inspect_result = d4_bishop.inspect_move(pieces, ChessCoord('E', '3'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True, [], e3_king))

    def test_taking_king_not_allowed_further_away(self):
        c4_rook = Rook(ChessCoord('C', '4'), black)
        c1_king = King(ChessCoord('C', '1'), white)
        pieces = [c4_rook, c1_king]
        move_inspect_result = c4_rook.inspect_move(pieces, ChessCoord('C', '1'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True,
                                          [GridCoord(2, 2),
                                           GridCoord(2, 1)], c1_king))

    def test_taking_king_not_allowed_pawn(self):
        a4_pawn = Pawn(ChessCoord('C', '4'), black, directions.go_south)
        b3_king = King(ChessCoord('B', '3'), white)
        pieces = [a4_pawn, b3_king]
        move_inspect_result = a4_pawn.inspect_move(pieces, ChessCoord('B', '3'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True,
                                          [], b3_king))

    def test_taking_king_not_allowed_knight(self):
        c5_knight = Knight(ChessCoord('C', '5'), black)
        b3_king = King(ChessCoord('B', '3'), white)
        pieces = [c5_knight , b3_king]
        move_inspect_result = c5_knight.inspect_move(pieces, ChessCoord('B', '3'))

        self.failUnless(move_inspect_result ==
                        MoveInspectResult(False, True,
                                          [], b3_king))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
