# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_rook, DirectionResult
import board_parts as bps


class Rook(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'R', '♖', move_directions_rook())
        else:
            Piece.__init__(self, chess_coord, black, 'R', '♜', move_directions_rook())
