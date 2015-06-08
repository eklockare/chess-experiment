# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white

class Pawn(Piece):
    def __init__(self, chess_coord, colour, move_direction):
        self.move_direction = move_direction
        if colour is white:
            Piece.__init__(self, chess_coord, colour, 'P', '♙')
        else:
            Piece.__init__(self, chess_coord, colour, 'P', '♟')

    def is_valid_move(self, pieces, move):
        return True