# -*- coding: utf-8 -*-
import unittest

from board_parts import ChessCoord, black, white
from pieces.king import King


class CheckTests(unittest.TestCase):
    def setUp(self):
        chess_coord_white = ChessCoord('E', '6')
        self.king_white = King(chess_coord_white, white)
        chess_coord_black = ChessCoord('G', '5')
        self.king_black = King(chess_coord_black, black)

    def test_no_king_negative_case_no_check(self):
        pass


def main():
    unittest.main()


if __name__ == '__main__':
    main()