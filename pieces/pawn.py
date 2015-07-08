# -*- coding: utf-8 -*-
import directions
import movement
from pieces.piece import Piece, find_possible_piece
from board_parts import white
from directions import go_north, go_south, is_diagonal_move, \
    get_direction, go_north_west, go_north_east, go_south_east, go_south_west
import board_parts as bps
from movement import MoveInspectResult

class Pawn(Piece):
    def __init__(self, chess_coord, colour, move_direction):
        if colour is white:
            Piece.__init__(self, chess_coord, colour, 'P', '♙', [move_direction])
        else:
            Piece.__init__(self, chess_coord, colour, 'P', '♟', [move_direction])
        self.en_passant_square = None

    def is_valid_taking_direction(self, take_direction):
        my_direction = self.move_directions[0]

        if my_direction == go_north:
            return take_direction in [go_north_east, go_north_west]
        else:
            return take_direction in [go_south_east, go_south_west]

    def inspect_taking_move(self, pieces, grid_move, move_direction):
        move_inspect_result_direction = \
            self.paths_and_piece_in_direction(self.grid_coord,
                grid_move,
                pieces,
                move_direction,
                [])

        pawns_that_have_en_passant_on_this_move = filter(lambda piece:
                                            piece.letter == 'P' and
                                            piece.en_passant_square and
                                            piece.en_passant_square == grid_move and
                                            piece != self,
                                            pieces)

        ok_num_of_steps = len(move_inspect_result_direction.squares) == 1
        valid_taking_direction = self.is_valid_taking_direction(move_direction )
        possible_piece = find_possible_piece(pieces, grid_move)
        if len(pawns_that_have_en_passant_on_this_move) == 1:
            possible_piece = pawns_that_have_en_passant_on_this_move[0]

        if ok_num_of_steps and valid_taking_direction and possible_piece:
            if possible_piece.colour == self.colour:
                return MoveInspectResult(False, True, [grid_move], possible_piece)
            else:
                return MoveInspectResult(True, False, [grid_move], possible_piece)
        else:
            return MoveInspectResult(False, False, [], None)

    def register_possible_en_passant(self, chess_coord):
        grid_move = bps.chess_coord_to_grid_coord(chess_coord)
        diff = grid_move.row - self.grid_coord.row

        if abs(diff) == 2:
            self.en_passant_square = self.move_directions[0](self.grid_coord)
        else:
            self.en_passant_square = None

    def update_coords(self, chess_coord):
        self.register_possible_en_passant(chess_coord)
        Piece.update_coords(self, chess_coord)

    def inspect_move(self, pieces, move):
        grid_move = bps.chess_coord_to_grid_coord(move)
        move_direction = get_direction(self.grid_coord, grid_move)

        if is_diagonal_move(move_direction):
            return self.inspect_taking_move(pieces, grid_move, move_direction)

        move_inspect_result = Piece.inspect_move(self, pieces, move)
        ok_num_of_steps = self.ok_number_steps(move_inspect_result.squares)

        move_inspect_result.is_valid_move = ok_num_of_steps and \
            move_inspect_result.is_valid_move

        if move_inspect_result.piece:
            move_inspect_result.is_valid_move = False
            move_inspect_result.was_blocked = True

        return move_inspect_result

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

    def __str__(self):
        return "Pawn(%s, %s, %s, %s, en_passant_square=%s) " % (self.colour,
                            self.move_directions,
                            self.chess_coord,
                            self.grid_coord,
                            self.en_passant_square)

    def __eq__(self, other):
        return self.grid_coord == other.grid_coord and \
            self.letter == other.letter and \
            self.colour == other.colour
