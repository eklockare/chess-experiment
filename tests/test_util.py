# -*- coding: utf-8 -*-
import unittest
from pieces.pawn import Pawn
from pieces.rook import Rook

import util
from board_parts import ChessCoord, GridCoord, black


class UtilTests(unittest.TestCase):

    def test_util_compare_value_lists(self):
        listone = [1, 2, 3]
        listtwo = [1, 2, 3]

        result = util.compare_lists(listone, listtwo)

        self.failUnless(result)

    def test_util_compare_value_lists_not_equal(self):
        listone = [1, 2, 3]
        listtwo = [1, 2, 3, 4]

        result = util.compare_lists(listone, listtwo)

        self.failIf(result)

    def test_util_compare_value_lists_chess_coord(self):
        listone = [ChessCoord('A', '2'), ChessCoord('A', '3')]
        listtwo = [ChessCoord('A', '3'), ChessCoord('A', '2')]

        result = util.compare_lists(listone, listtwo)

        self.failUnless(result)

    def test_util_compare_value_lists_grid_coord(self):
        listone = [GridCoord(2, 4), GridCoord(0, 1)]
        listtwo = [GridCoord(0, 1), GridCoord(2, 4)]

        result = util.compare_lists(listone, listtwo)

        self.failUnless(result)

    def test_util_compare_value_lists_grid_coord_not_equal(self):
        listone = [GridCoord(2, 4), GridCoord(0, 2)]
        listtwo = [GridCoord(0, 1), GridCoord(2, 4)]

        result = util.compare_lists(listone, listtwo)

        self.failIf(result)

    def test_util_compare_value_lists_chess_coord_not_equal(self):
        listone = [ChessCoord('C', '4'), ChessCoord('B', '2')]
        listtwo = [ChessCoord('B', '2'), ChessCoord('A', '4')]

        result = util.compare_lists(listone, listtwo)

        self.failIf(result)

    def test_util_compare_value_lists_grid_coord_long(self):
        listone = [
            GridCoord(6, 5),
            GridCoord(5, 5),
            GridCoord(3, 5),
            GridCoord(2, 5),
            GridCoord(1, 5),
            GridCoord(0, 5)]
        listtwo = [
            GridCoord(6, 5),
            GridCoord(5, 5),
            GridCoord(3, 5),
            GridCoord(2, 5),
            GridCoord(1, 5),
            GridCoord(0, 5)]

        result = util.compare_lists(listone, listtwo)

        self.failUnless(result)

    def test_util_compare_value_lists_one_extra(self):
        listone = [
            GridCoord(6, 5),
            GridCoord(6, 5),
            GridCoord(5, 5),
            GridCoord(3, 5),
            GridCoord(2, 5),
            GridCoord(1, 5),
            GridCoord(0, 5)]
        listtwo = [
            GridCoord(6, 5),
            GridCoord(5, 5),
            GridCoord(3, 5),
            GridCoord(2, 5),
            GridCoord(1, 5),
            GridCoord(0, 5)]

        result = util.compare_lists(listone, listtwo)
        result_reversed = util.compare_lists(listtwo, listone)

        self.failIf(result)
        self.failIf(result_reversed)

    def test_util_compare_value_lists_chess_coord_same(self):
        listone = [
            ChessCoord('E', '6'),
            ChessCoord('E', '8')]
        listtwo = [
            ChessCoord('E', '8'),
            ChessCoord('E', '8')]

        result = util.compare_lists(listone, listtwo)
        self.failIf(result)

    def test_select_piece(self):
        rook = Rook(ChessCoord('A', '1'), black)
        pieces = [rook]
        chess_coord = ChessCoord('A', '1')
        selection = util.select_piece(chess_coord, pieces)
        self.failUnless(selection == rook)

        chess_coord = GridCoord(0, 0)
        selection = util.select_piece(chess_coord, pieces)
        self.failUnless(selection == rook)

        chess_coord = GridCoord(0, 1)
        selection = util.select_piece(chess_coord, pieces)
        self.failUnless(selection is None)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
