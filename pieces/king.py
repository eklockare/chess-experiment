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

    def check_all_directions(self, pieces, move_to):
        move_check_results = Piece.check_all_directions(self, pieces, move_to)

        for mir in move_check_results:
            if len(mir.squares) > 1:
                mir.is_valid_move = False
                mir.possible_piece = None

        return move_check_results
