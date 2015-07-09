# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_queen


class Queen(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'Q', '♕', move_directions_queen())
        else:
            Piece.__init__(self, chess_coord, black, 'Q', '♛', move_directions_queen())
