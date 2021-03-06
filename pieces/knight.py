# -*- coding: utf-8 -*-
from pprint import pprint
from move_inspect_result import MoveInspectResult
from pieces.piece import Piece
from board_parts import white, black
from directions import move_directions_knight
import board_parts as bps
from util import select_piece


class Knight(Piece):
    def __init__(self, chess_coord, colour):
        if colour is white:
            Piece.__init__(self, chess_coord, white, 'Kn', '♘', move_directions_knight())
        else:
            Piece.__init__(self, chess_coord, black, 'Kn', '♞', move_directions_knight())

    def get_all_destinations(self):
        all_destinations = map(lambda move_direction:
                               move_direction(self.grid_coord),
                               self.move_directions)
        return filter(lambda dest: dest is not None, all_destinations)

    def inspect_move(self, pieces, move):
        all_destinations = self.get_all_destinations()

        grid_move = bps.chess_coord_to_grid_coord(move)

        possible_piece = select_piece(grid_move, pieces)

        valid_move = grid_move in all_destinations

        move_inspect_result = MoveInspectResult(valid_move, False, [], possible_piece)

        if possible_piece:
            if possible_piece.colour == self.colour or \
                    self.piece_is_enemy_king(possible_piece):
                move_inspect_result.was_blocked = True
                move_inspect_result.is_valid_move = False

        move_inspect_result.will_put_self_in_check = \
                self.check_for_putting_self_in_check(pieces,
                                                     move,
                                                     move_inspect_result)
        move_inspect_result.is_valid_move = move_inspect_result.is_valid_move and \
                                            not move_inspect_result.will_put_self_in_check

        return move_inspect_result

    def add_possible_pieces_and_squares_to_threat_list(self, pieces):
        all_destinations = self.get_all_destinations()
        self.is_threat_to_these_pieces = filter(lambda piece:
                                                piece.grid_coord in
                                                all_destinations
                                                and piece.colour !=
                                                self.colour, pieces)

        grids_threatened_pieces = map(lambda piece: piece.grid_coord, self.is_threat_to_these_pieces)
        self.is_threat_to_these_squares = filter(lambda dest_grid_coord:
                                                 dest_grid_coord not in grids_threatened_pieces,
                                                 all_destinations)
