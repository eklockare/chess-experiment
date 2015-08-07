# -*- coding: utf-8 -*-
import unittest

from board_parts import ChessCoord, black, white
from move_inspect_result import MoveInspectResult
from pieces.bishop import Bishop
from pieces.king import King
from starting_pieces import starting_pieces
from util import select_piece
import copy

class CheckTests(unittest.TestCase):
    def setUp(self):
        self.king_white = King(ChessCoord('E', '6'), white)
        self.king_black = King(ChessCoord('G', '5'), black)
        self.bishop_black = Bishop(ChessCoord('B', '4'), black)
        self.rook_white = Bishop(ChessCoord('A', '2'), white)
        self.pieces = [self.king_black, self.king_white,
                       self.bishop_black, self.rook_white]
        self.move_inspect_result_no_piece = MoveInspectResult(True, False, [], None)

    def test_check_no_false_positive(self):
        is_in_check = self.king_black.check_for_putting_self_in_check(self.pieces,
                                                                      ChessCoord('F', '4'),
                                                                      self.move_inspect_result_no_piece)
        self.failIf(is_in_check)

    def test_king_moves_into_check_detected(self):
        is_in_check = self.king_white.check_for_putting_self_in_check(self.pieces,
                                                                      ChessCoord('E', '7'),
                                                                      self.move_inspect_result_no_piece)

        self.failUnless(is_in_check)

    def test_piece_moves_and_puts_own_king_into_check(self):
        self.bishop_black.update_coord(ChessCoord('B', '3'))
        self.rook_white.update_coord(ChessCoord('D', '5'))
        is_in_check = self.rook_white.check_for_putting_self_in_check(self.pieces,
                                                                      ChessCoord('D', '6'),
                                                                      self.move_inspect_result_no_piece)
        self.failUnless(is_in_check)

    def test_with_full_pieces_block_check(self):
        all_pieces = copy.deepcopy(starting_pieces)
        # move e2 white pawn
        e2_pawn = select_piece(ChessCoord('E', '2'), all_pieces)
        is_in_check = e2_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('E', '4'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        e2_pawn.update_coord(ChessCoord('E', '4'))

        # move black pawn d6
        d7_pawn = select_piece(ChessCoord('D', '7'), all_pieces)
        is_in_check = d7_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('D', '6'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        d7_pawn.update_coord(ChessCoord('D', '6'))

        # move black bishop g4
        c8_bishop = select_piece(ChessCoord('C', '8'), all_pieces)
        is_in_check = c8_bishop.check_for_putting_self_in_check(all_pieces,
                                                                ChessCoord('G', '4'),
                                                                self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        c8_bishop.update_coord(ChessCoord('G', '4'))

        # move white king to e2
        e1_king = select_piece(ChessCoord('E', '1'), all_pieces)
        is_in_check = e1_king.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('E', '2'),
                                                              self.move_inspect_result_no_piece)
        self.failUnless(is_in_check)
        e1_king.update_coord(ChessCoord('E', '2'))

        # move white pawn to f3
        f2_pawn = select_piece(ChessCoord('F', '2'), all_pieces)
        is_in_check = f2_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('F', '3'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        f2_pawn.update_coord(ChessCoord('F', '3'))

    def test_with_full_pieces_take_checking_piece(self):
        all_pieces = copy.deepcopy(starting_pieces)
        # move e2 white pawn
        e2_pawn = select_piece(ChessCoord('E', '2'), all_pieces)
        is_in_check = e2_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('E', '4'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        e2_pawn.update_coord(ChessCoord('E', '4'))

        # move d7 pawn to d6
        d7_pawn = select_piece(ChessCoord('D', '7'), all_pieces)
        is_in_check = d7_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('D', '6'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        d7_pawn.update_coord(ChessCoord('D', '6'))

        # move f1 bishop to b5
        f1_bishop = select_piece(ChessCoord('F', '1'), all_pieces)
        is_in_check = f1_bishop.check_for_putting_self_in_check(all_pieces,
                                                                ChessCoord('B', '5'),
                                                                self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        f1_bishop.update_coord(ChessCoord('B', '5'))

        # move c7 pawn to c6
        c7_pawn = select_piece(ChessCoord('C', '7'), all_pieces)
        is_in_check = c7_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('C', '6'),
                                                              self.move_inspect_result_no_piece)
        self.failIf(is_in_check)
        c7_pawn.update_coord(ChessCoord('C', '6'))

        # move b5 bishop to c6 take
        b5_bishop = select_piece(ChessCoord('B', '5'), all_pieces)
        is_in_check = b5_bishop.check_for_putting_self_in_check(all_pieces,
                                                                ChessCoord('C', '6'),
                                                                MoveInspectResult(True, False, [], c7_pawn))
        self.failIf(is_in_check)
        b5_bishop.update_coord(ChessCoord('C', '6'))
        all_pieces.remove(c7_pawn)

        # move b7 to c6
        b7_pawn = select_piece(ChessCoord('B', '7'), all_pieces)
        is_in_check = b7_pawn.check_for_putting_self_in_check(all_pieces,
                                                              ChessCoord('C', '6'),
                                                              MoveInspectResult(True, False, [], b5_bishop))
        self.failIf(is_in_check)
        b7_pawn.update_coord(ChessCoord('C', '6'))
        all_pieces.remove(b5_bishop)

    def test_king_takes_checking_piece_and_can_keep_moving(self):
        all_pieces = copy.deepcopy(starting_pieces)
        d2_pawn = select_piece(ChessCoord('D', '2'), all_pieces)
        e7_pawn = select_piece(ChessCoord('E', '7'), all_pieces)
        f8_bishop = select_piece(ChessCoord('F', '8'), all_pieces)
        d1_queen = select_piece(ChessCoord('D', '1'), all_pieces)
        e1_king = select_piece(ChessCoord('E', '1'), all_pieces)

        d2_pawn.inspect_move(all_pieces, ChessCoord('D', '4'))
        d2_pawn.update_coord(ChessCoord('D', '4'))

        e7_pawn.inspect_move(all_pieces, ChessCoord('E', '6'))
        e7_pawn.update_coord(ChessCoord('E', '6'))

        f8_bishop.inspect_move(all_pieces, ChessCoord('B', '4'))
        f8_bishop.update_coord(ChessCoord('B', '4'))

        move_inspect_result = d1_queen.inspect_move(all_pieces, ChessCoord('D', '2'))
        self.failIf(move_inspect_result.will_put_self_in_check)
        d1_queen.update_coord(ChessCoord('D', '2'))

        f8_bishop.inspect_move(all_pieces, ChessCoord('D', '2'))
        f8_bishop.update_coord(ChessCoord('D', '2'))

        all_pieces.remove(d1_queen)

        move_inspect_result = e1_king.inspect_move(all_pieces, ChessCoord('D', '2'))
        self.failIf(move_inspect_result.will_put_self_in_check)
        e1_king.update_coord(ChessCoord('D', '2'))

        all_pieces.remove(f8_bishop)

        move_inspect_result = e1_king.inspect_move(all_pieces, ChessCoord('D', '3'))
        self.failIf(move_inspect_result.will_put_self_in_check)
        self.failUnless(move_inspect_result.is_valid_move)
        e1_king.update_coord(ChessCoord('D', '3'))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
