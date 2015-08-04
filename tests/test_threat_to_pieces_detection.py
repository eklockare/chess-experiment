# -*- coding: utf-8 -*-
import unittest
from board_parts import ChessCoord, white, black
from directions import go_north
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
from starting_pieces import starting_pieces
from util import select_piece, select_pieces
import util
import copy

class ThreatTests(unittest.TestCase):
    def setUp(self):
        self.queen_white = Queen(ChessCoord('E', '6'), white)
        self.queen_black = Queen(ChessCoord('G', '5'), black)
        self.rook_white = Rook(ChessCoord('D', '1'), white)
        self.knight_white = Knight(ChessCoord('G', '1'), white)
        self.pieces = [self.queen_white, self.queen_black, self.rook_white,
                       self.knight_white]

    def test_queens_threatening_each_other(self):
        self.queen_white.analyze_threats_on_board_for_new_move(self.pieces,
                                                               ChessCoord('E', '5'))

        self.failUnless(self.queen_black.is_threat_to_these_pieces ==
                        [self.queen_white, self.knight_white])
        self.failUnless(self.queen_white.is_threat_to_these_pieces ==
                        [self.queen_black])

    def test_queen_threatening_rook_but_not_vice_versa(self):
        self.queen_black.analyze_threats_on_board_for_new_move(self.pieces,
                                                               ChessCoord('G', '4'))

        self.failUnless(self.queen_black.is_threat_to_these_pieces ==
                        [self.queen_white, self.rook_white, self.knight_white])
        self.failUnless(self.queen_white.is_threat_to_these_pieces ==
                        [self.queen_black])
        self.failUnless(self.rook_white.is_threat_to_these_pieces ==
                        [])

    def test_knight_threatening_queen_but_not_vice_versa(self):
        self.knight_white.analyze_threats_on_board_for_new_move(self.pieces,
                                                                ChessCoord('F', '3'))

        self.failUnless(self.knight_white.is_threat_to_these_pieces ==
                        [self.queen_black])
        self.failUnless(self.queen_black.is_threat_to_these_pieces == [])

    def test_knight_threatening_none(self):
        pieces = self.pieces + [Pawn(ChessCoord('C', '3'), black, go_north),
                                Knight(ChessCoord('C', '1'), black),
                                ]
        self.knight_white.update_coord(ChessCoord('A', '4'))
        self.knight_white.analyze_threats_on_board_for_new_move(pieces,
                                                                ChessCoord('B', '2'))

        self.failUnless(self.knight_white.is_threat_to_these_pieces ==
                        [])

    def test_knight_threatening_none_with_all_pieces(self):
        pieces = copy.deepcopy(starting_pieces)
        g8_knight = select_piece(ChessCoord('G', '8'), pieces)
        e2_pawn = select_piece(ChessCoord('E', '2'), pieces)
        e2_pawn.analyze_threats_on_board_for_new_move(pieces,
                                                      ChessCoord('E', '4'))

        self.failUnless(g8_knight.is_threat_to_these_pieces ==
                        [])

    def test_king_only_threatens_for_one_step_with_all_pieces(self):
        pieces = copy.deepcopy(starting_pieces)
        e1_king = select_piece(ChessCoord('E', '1'), pieces)
        e1_king.analyze_threats_on_board_for_new_move(pieces,
                                                      ChessCoord('E', '6'))

        pawns_d7_e7_f7 = select_pieces([ChessCoord('D', '7'),
                                        ChessCoord('E', '7'),
                                        ChessCoord('F', '7')], pieces)

        self.failUnless(util.compare_lists(e1_king.is_threat_to_these_pieces,
                                           pawns_d7_e7_f7))

    def test_pieces_threatens_none_from_start_position(self):
        pieces = copy.deepcopy(starting_pieces)
        map(lambda piece: piece.analyze_threats_on_board_for_new_move(pieces,
                                                                      piece.chess_coord
                                                                      ), pieces)
        all_threats = map(lambda piece: piece.is_threat_to_these_pieces, pieces)

        should_be_all_empty = filter(lambda threat_list: threat_list is not [], all_threats)

        should_be_all_empty_filter_away_empty = map(lambda sbae: sbae is not [],
                                                    should_be_all_empty)
        self.failIf(False in should_be_all_empty_filter_away_empty)

    def test_pawn_threatens_none_from_start_position(self):
        pieces = copy.deepcopy(starting_pieces)
        b7_pawn = select_piece(ChessCoord('B', '7'), pieces)
        b7_pawn.analyze_threats_on_board_for_new_move(pieces,
                                                      ChessCoord('B', '7'))

        self.failUnless(b7_pawn.is_threat_to_these_pieces == [])

    def test_pawn_threatens_appropriate_pieces_in_front_of_it(self):
        pieces = copy.deepcopy(starting_pieces)
        f2_pawn = select_piece(ChessCoord('F', '2'), pieces)
        f2_pawn.analyze_threats_on_board_for_new_move(pieces,
                                                      ChessCoord('F', '6'))

        pawns_e7_g7 = select_pieces([ChessCoord('E', '7'),
                                     ChessCoord('G', '7')], pieces)

        self.failUnless(util.compare_lists(f2_pawn.is_threat_to_these_pieces,
                                           pawns_e7_g7))

    def test_pawn_threatens_appropriate_pieces_with_en_passant_in_front_of_it(self):
        pieces = copy.deepcopy(starting_pieces)
        g7_pawn = select_piece(ChessCoord('G', '7'), pieces)
        g7_pawn.update_coord(ChessCoord('G', '5'))

        f2_pawn = select_piece(ChessCoord('F', '2'), pieces)
        f2_pawn.analyze_threats_on_board_for_new_move(pieces,
                                                      ChessCoord('F', '5'))

        self.failUnless(util.compare_lists(f2_pawn.is_threat_to_these_pieces,
                                           [g7_pawn]))
def main():
    unittest.main()

if __name__ == '__main__':
    main()
