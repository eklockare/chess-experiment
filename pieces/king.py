# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_queen


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
