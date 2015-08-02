# -*- coding: utf-8 -*-
import unittest
from board_parts import ChessCoord, white, black, GridCoord, chess_coord_to_grid_coord, grid_coord_to_chess_coord
from directions import go_north, go_south
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
        pass

    def test_queen_threat_empty_board(self):
        queen_white = Queen(ChessCoord('E', '6'), white)
        pieces = [queen_white]
        queen_white.analyze_threats_on_board_for_new_move(pieces,
                                                          ChessCoord('E', '5'))

        expected_squares_chess = [
            ChessCoord('E', '6'),  # north
            ChessCoord('E', '7'),
            ChessCoord('E', '8'),

            ChessCoord('E', '4'),  # south
            ChessCoord('E', '3'),
            ChessCoord('E', '2'),
            ChessCoord('E', '1'),

            ChessCoord('D', '5'),  # east
            ChessCoord('C', '5'),
            ChessCoord('B', '5'),
            ChessCoord('A', '5'),

            ChessCoord('F', '5'),  # west
            ChessCoord('G', '5'),
            ChessCoord('H', '5'),

            ChessCoord('D', '4'),  # south west
            ChessCoord('C', '3'),
            ChessCoord('B', '2'),
            ChessCoord('A', '1'),

            ChessCoord('D', '6'),  # north west
            ChessCoord('C', '7'),
            ChessCoord('B', '8'),

            ChessCoord('F', '6'),  # north east
            ChessCoord('G', '7'),
            ChessCoord('H', '8'),

            ChessCoord('F', '4'),  # south east
            ChessCoord('G', '3'),
            ChessCoord('H', '2'),
        ]
        expected_squares_grid = map(chess_coord_to_grid_coord, expected_squares_chess)

        self.failUnless(util.compare_lists(expected_squares_grid,
                                           queen_white.is_threat_to_these_squares))

    def test_queen_threat_blocking_pieces(self):
        queen_white = Queen(ChessCoord('E', '6'), white)
        rook_white = Rook(ChessCoord('E', '7'), white)

        pawn_black = Pawn(ChessCoord('A', '1'), black, go_south)
        pieces = [queen_white, pawn_black, rook_white]
        queen_white.analyze_threats_on_board_for_new_move(pieces,
                                                          ChessCoord('E', '5'))

        expected_squares_chess = [
            ChessCoord('E', '6'), # north
            # rest blocked

            ChessCoord('E', '4'),  # south
            ChessCoord('E', '3'),
            ChessCoord('E', '2'),
            ChessCoord('E', '1'),

            ChessCoord('D', '5'),  # east
            ChessCoord('C', '5'),
            ChessCoord('B', '5'),
            ChessCoord('A', '5'),

            ChessCoord('F', '5'),  # west
            ChessCoord('G', '5'),
            ChessCoord('H', '5'),

            ChessCoord('D', '4'),  # south west
            ChessCoord('C', '3'),
            ChessCoord('B', '2'),
            # blocked: ChessCoord('A', '1'),

            ChessCoord('D', '6'),  # north west
            ChessCoord('C', '7'),
            ChessCoord('B', '8'),

            ChessCoord('F', '6'),  # north east
            ChessCoord('G', '7'),
            ChessCoord('H', '8'),

            ChessCoord('F', '4'),  # south east
            ChessCoord('G', '3'),
            ChessCoord('H', '2'),
        ]
        expected_squares_grid = map(chess_coord_to_grid_coord, expected_squares_chess)
        self.failUnless(util.compare_lists(expected_squares_grid,
                                           queen_white.is_threat_to_these_squares))

    def test_rook_threat_squares_blocking_pieces(self):
        queen_white = Queen(ChessCoord('A', '4'), white)
        rook_white = Rook(ChessCoord('F', '4'), white)

        pawn_black_1 = Pawn(ChessCoord('F', '5'), black, go_south)
        pawn_black_2 = Pawn(ChessCoord('H', '4'), black, go_south)
        pieces = [queen_white, pawn_black_1, pawn_black_2, rook_white]
        rook_white.analyze_threats_on_board_for_new_move(pieces,
                                                         ChessCoord('F', '4'))

        expected_squares_chess = [  # north

            ChessCoord('F', '3'),  # south
            ChessCoord('F', '2'),
            ChessCoord('F', '1'),

            ChessCoord('B', '4'),  # west
            ChessCoord('C', '4'),
            ChessCoord('D', '4'),
            ChessCoord('E', '4'),

            ChessCoord('G', '4'),  # east
        ]

        expected_squares_grid = map(chess_coord_to_grid_coord, expected_squares_chess)

        self.failUnless(util.compare_lists(expected_squares_grid,
                                           rook_white.is_threat_to_these_squares))



def main():
    unittest.main()


if __name__ == '__main__':
    main()
