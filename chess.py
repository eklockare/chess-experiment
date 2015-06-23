# -*- coding: utf-8 -*-
import board_parts as bps
import drawing as dr
import movement as mov
from board_parts import ChessCoord, GridCoord, chess_coord_to_grid_coord
import directions as dirs
import collision as col
from pieces.piece import Piece

INPUT_LENGTH = 2



def valid_coordinates(col, row):
    return col in bps.CHESS_TO_GRID_COLUMNS and row in bps.CHESS_TO_GRID_ROWS


def validate_input(user_input, select_or_move):
    if len(user_input) is 0:
        return None, 'cancel'
    elif len(user_input) is not INPUT_LENGTH:
        return None, bps.yellow("invalid input, one letter and one number required, ex: A1.\n") \
               + select_or_move

    col, row = user_input[0], user_input[1]

    if not valid_coordinates(col, row):
        return None, bps.yellow("Invalid coordinates: " +
                                str((col, row)) +
                                str(" A-H + 1-8 required\n")) + \
               select_or_move
    else:
        return col, row


def game_loop(pieces, last_move, piece_to_move):
    def select_piece(pieces, last_move, msg):
        dr.draw_board(pieces, last_move)

        if msg:
            print msg

        user_input = raw_input()
        user_input = user_input.upper()
        col, row = validate_input(user_input, "Select piece")

        if not col:
            if row is 'cancel':
                select_piece(pieces, None, "Cancelled selection")
            else:
                msg = row
                select_piece(pieces, last_move, msg)

        piece_selection = filter(lambda piece: piece.chess_coord.col is col and piece.chess_coord.row is row, pieces)

        if piece_selection:
            selected_piece = piece_selection[0]
            last_move = chess_coord_to_grid_coord(selected_piece.chess_coord), None
            game_loop(pieces, last_move, selected_piece)

        else:
            select_piece(pieces, last_move, bps.yellow("no piece on that square\n") + "Select piece")

    def move_piece(pieces, last_move, msg):
        dr.draw_board(pieces, last_move)

        if msg:
            print msg

        user_input = raw_input()
        user_input = user_input.upper()
        input_result = validate_input(user_input, "Move piece ")
        col_new, row_new = input_result
        new_coordinates = ChessCoord(col_new, row_new)

        if not col_new:
            if row_new is 'cancel':
                select_piece(pieces, None, "cancelled")
            else:
                _, msg = input_result
                move_piece(pieces, last_move, msg)

        # check if move is valid here
        # is valid for this piece
        is_valid_movement, possible_moves = \
            mov.is_valid_movement_pattern_for_piece(piece_to_move,
                                                    new_coordinates,
                                                    pieces)
        # puts us in check
        # check if there is a piece on moved to square, if so remove it, or deny if own piece
        is_valid_movement, is_blocked, piece_to_take, msg, possible_moves = col.check_if_move_is_blocked(
            piece_to_move,
            col_new,
            row_new,
            possible_moves,
            pieces)


        if not is_valid_movement:
            move_piece(pieces, last_move, "Invalid move for this piece")
        else:


            if is_blocked:
                move_piece(pieces, last_move, msg)
            else:
                if piece_to_take:
                    pieces.remove(piece_to_take)

                piece_to_move.update_coords(new_coordinates )
                last_move = chess_coord_to_grid_coord(piece_to_move.chess_coord), \
                            chess_coord_to_grid_coord(new_coordinates)
                game_loop(pieces, last_move, None)

    if piece_to_move:
        move_piece(pieces, last_move, "Move piece")
    else:
        select_piece(pieces, last_move, "Select piece")


starting_pieces = [
    # black pawns
    Piece(ChessCoord('A', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('B', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('C', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('D', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('E', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('F', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('G', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    Piece(ChessCoord('H', '7'), bps.black, 'P', '♟', [dirs.go_south]),
    # black back row
    Piece(ChessCoord('A', '8'), bps.black, 'R', '♜', dirs.move_directions_rook()),
    Piece(ChessCoord('B', '8'), bps.black, 'Kn', '♞', dirs.move_directions_knight()),
    Piece(ChessCoord('C', '8'), bps.black, 'B', '♝', dirs.move_directions_bishop()),
    Piece(ChessCoord('D', '8'), bps.black, 'Q', '♛', dirs.move_directions_queen()),
    Piece(ChessCoord('E', '8'), bps.black, 'K', '♚', dirs.move_directions_queen()),
    Piece(ChessCoord('F', '8'), bps.black, 'B', '♝', dirs.move_directions_bishop()),
    Piece(ChessCoord('G', '8'), bps.black, 'Kn', '♞', dirs.move_directions_knight()),
    Piece(ChessCoord('H', '8'), bps.black, 'R', '♜', dirs.move_directions_rook()),
    # white pawns
    Piece(ChessCoord('A', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('B', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('C', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('D', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('E', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('F', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('G', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    Piece(ChessCoord('H', '2'), bps.white, 'P', '♙', [dirs.go_north]),
    # white back row
    Piece(ChessCoord('A', '1'), bps.white, 'R', '♖', dirs.move_directions_rook()),
    Piece(ChessCoord('B', '1'), bps.white, 'Kn', '♘', dirs.move_directions_knight()),
    Piece(ChessCoord('C', '1'), bps.white, 'B', '♗', dirs.move_directions_bishop()),
    Piece(ChessCoord('D', '1'), bps.white, 'Q', '♕', dirs.move_directions_queen()),
    Piece(ChessCoord('E', '1'), bps.white, 'K', '♔', dirs.move_directions_queen()),
    Piece(ChessCoord('F', '1'), bps.white, 'B', '♗', dirs.move_directions_bishop()),
    Piece(ChessCoord('G', '1'), bps.white, 'Kn', '♘', dirs.move_directions_knight()),
    Piece(ChessCoord('H', '1'), bps.white, 'R', '♖', dirs.move_directions_rook()),
]
game_loop(starting_pieces, None, None)