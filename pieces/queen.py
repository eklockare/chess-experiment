# -*- coding: utf-8 -*-
from movement import go_max_distances
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_queen, is_within_board, DirectionResult
import board_parts as bps
import util

class Queen(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'Q', '♕', move_directions_queen())
        else:
            Piece.__init__(self, chess_coord, black, 'Q', '♛', move_directions_queen())

    def paths_and_piece_in_direction(self, from_coord, pieces, direction, squares):
        new_coord_grid = direction(from_coord)
        possible_piece = filter(lambda piece: piece.grid_coord == new_coord_grid, pieces)

        if not new_coord_grid:
            return DirectionResult(squares, None)
        elif possible_piece:
            return DirectionResult(squares, possible_piece)
        else:
            squares.append(new_coord_grid)
            return self.paths_and_piece_in_direction(new_coord_grid, pieces, direction, squares)

    def check_all_directions(self, pieces):
        possible_moves = map(lambda direction:
                             self.paths_and_piece_in_direction(self.grid_coord, pieces, direction, []),
                             self.move_directions)
        return possible_moves

    def is_valid_move(self, pieces, move):
        move_grid = bps.chess_coord_to_grid_coord(move)
        direction_results = self.check_all_directions(pieces)

        match = filter(lambda direction_result: move_grid in
                       direction_result.squares,
                       direction_results)

        return len(match) == 1
