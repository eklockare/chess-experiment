# -*- coding: utf-8 -*-
from movement import go_max_distances
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_queen, is_within_board, DirectionResult
import board_parts as bps
import util

class King(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'K', '♔', move_directions_queen())
        else:
            Piece.__init__(self, chess_coord, black, 'K', '♚', move_directions_queen())

    def inspect_move(self, pieces, move):
        move_inspect_result = Piece.inspect_move(self, pieces, move)

        move_inspect_result.is_valid_move = move_inspect_result.is_valid_move and \
            len(move_inspect_result.squares) == 1

        return move_inspect_result