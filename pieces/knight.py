# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_knight
import board_parts as bps


class Knight(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'Kn', '♘', move_directions_knight())
        else:
            Piece.__init__(self, chess_coord, black, 'Kn', '♞', move_directions_knight())

    def is_valid_move(self, pieces, move):
        all_destinations = map(lambda move_direction:
                               move_direction(self.grid_coord),
                               move_directions_knight())
        clean_all_destinations = filter(lambda dest: dest, all_destinations)

        grid_move = bps.chess_coord_to_grid_coord(move)

        return grid_move in clean_all_destinations