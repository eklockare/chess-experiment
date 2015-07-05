# -*- coding: utf-8 -*-
from movement import MoveInspectResult
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_knight, DirectionResult
import board_parts as bps


class Knight(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'Kn', '♘', move_directions_knight())
        else:
            Piece.__init__(self, chess_coord, black, 'Kn', '♞', move_directions_knight())

    def inspect_move(self, pieces, move):
        all_destinations = map(lambda move_direction:
                               move_direction(self.grid_coord),
                               self.move_directions)
        clean_all_destinations = filter(lambda dest: dest, all_destinations)

        grid_move = bps.chess_coord_to_grid_coord(move)

        possible_piece = self.find_possible_piece(pieces, grid_move)

        valid_move = grid_move in clean_all_destinations

        move_result = MoveInspectResult(valid_move, False, [], possible_piece)

        if possible_piece:
            if possible_piece.colour == self.colour:
                move_result.was_blocked = True
                move_result.is_valid_move = False
            else:
                move_result.is_valid_move = True

        return move_result
