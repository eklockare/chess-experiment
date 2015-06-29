# -*- coding: utf-8 -*-
from pieces.piece import Piece
from board_parts import white
from directions import go_north, go_south, DirectionResult
import board_parts as bps
from movement import MoveResult

class Pawn(Piece):
    def __init__(self, chess_coord, colour, move_direction):
        if colour is white:
            Piece.__init__(self, chess_coord, colour, 'P', '♙', [move_direction])
        else:
            Piece.__init__(self, chess_coord, colour, 'P', '♟', [move_direction])

    def is_valid_move(self, pieces, move):
        grid_move = bps.chess_coord_to_grid_coord(move)
        valid_direction, direction, squares = \
            self.get_direction_and_squares(grid_move)
        if valid_direction:
            possible_piece = self.find_possible_piece(pieces, grid_move)

            return MoveResult(self.ok_number_steps(squares),
                              DirectionResult(squares, possible_piece))
        else:
            return MoveResult(False, DirectionResult(squares, None))

    def ok_number_steps(self, squares):
        on_start_row = self.is_on_start_row()

        if on_start_row:
            number_of_steps_allowed = 2
        else:
            number_of_steps_allowed = 1

        number_of_steps_in_move = len(squares)

        return (number_of_steps_in_move <= number_of_steps_allowed)

    def is_on_start_row(self):
        if self.move_directions == [go_north]:
            return self.grid_coord.row == 1
        else:
            return self.grid_coord.row == 6
