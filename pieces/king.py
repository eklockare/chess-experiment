# -*- coding: utf-8 -*-
from castling_moves_definition import castling_moves_squares_and_rook_coord_dict
from move_inspect_result import MoveInspectResult, CastlingMoveInspectResult
from pieces.piece import Piece
from board_parts import white, black, ChessCoord, chess_coord_to_grid_coord
from directions import move_directions_queen
from util import select_piece, select_pieces
import util


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

    def check_for_putting_self_in_check(self, pieces, new_coordinates, move_inspect_result):
        if move_inspect_result.was_castling_attempt and \
                move_inspect_result.is_valid_move:
            rook_old_coord = move_inspect_result.castling_rook.chess_coord
            new_coord_rook = move_inspect_result.new_coord_rook
            move_inspect_result.castling_rook.update_coord(new_coord_rook)
            check_result = Piece.check_for_putting_self_in_check(self,
                                                                 pieces,
                                                                 new_coordinates,
                                                                 move_inspect_result)

            move_inspect_result.castling_rook.update_coord(rook_old_coord)
            return check_result
        else:
            return Piece.check_for_putting_self_in_check(self,
                                                         pieces,
                                                         new_coordinates,
                                                         move_inspect_result)

    def inspect_move(self, pieces, move):
        castling_move_result = self.get_castling_move_result(pieces, move)
        if castling_move_result.was_castling_attempt:
            return castling_move_result
        else:
            return Piece.inspect_move(self, pieces, move)

    def get_castling_move_result(self, pieces, move):
        def get_valid_rook(coord):
            if coord:
                rook = select_piece(coord, pieces)
                if rook and rook.number_of_moves == 0 and rook.letter == 'R':
                    return rook
            return None

        def pieces_are_on_squares(squares, pieces):
            selection_result = select_pieces(squares, pieces)
            found_pieces = filter(lambda sr: sr is not None, selection_result)
            return found_pieces != []

        castling_inspect_result = CastlingMoveInspectResult(False, False,
                                                            False, False,
                                                            None, None)
        if str(move) in castling_moves_squares_and_rook_coord_dict:
            castling_squares_and_rook_coord = \
                castling_moves_squares_and_rook_coord_dict[str(move)]
        else:
            return castling_inspect_result

        if not (self.chess_coord == ChessCoord('E', '1') or
                        self.chess_coord == ChessCoord('E', '8')):
            return castling_inspect_result

        castling_inspect_result.was_castling_attempt = True

        rook_coord = castling_squares_and_rook_coord['rook_coord']
        possible_rook = get_valid_rook(rook_coord)

        squares_in_between = castling_squares_and_rook_coord['squares_in_between']

        grid_squares_in_between = map(chess_coord_to_grid_coord, squares_in_between)
        self.analyze_threats_on_board_for_new_move(pieces, self.chess_coord)

        threatened_squares = self.get_all_squares_the_enemy_threatens(pieces)
        squares_in_between_threatened = True in map(lambda inbetween_square:
                                                        inbetween_square in threatened_squares,
                                                        grid_squares_in_between)

        castling_inspect_result.was_blocked = pieces_are_on_squares(
            squares_in_between, pieces)

        has_not_moved = self.number_of_moves == 0
        is_in_check = Piece.check_if_own_king_in_check(self, pieces)

        is_valid_castling = possible_rook is not None and has_not_moved and \
                            not castling_inspect_result.was_blocked and not \
                            squares_in_between_threatened and not is_in_check

        castling_inspect_result.is_valid_move = is_valid_castling
        castling_inspect_result.castling_rook = possible_rook
        castling_inspect_result.new_coord_rook = \
            castling_squares_and_rook_coord['new_rook_coord']
        castling_inspect_result.squares_in_between_threatened = \
            squares_in_between_threatened

        return castling_inspect_result
