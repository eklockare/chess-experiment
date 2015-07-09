# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_bishop


class Bishop(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'B', '♗', move_directions_bishop())
        else:
            Piece.__init__(self, chess_coord, black, 'B', '♝', move_directions_bishop())
