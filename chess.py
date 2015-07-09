# -*- coding: utf-8 -*-
import board_parts as bps
import drawing as dr
import movement as mov
from board_parts import ChessCoord, GridCoord, chess_coord_to_grid_coord
import directions as dirs
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook

INPUT_LENGTH = 2



def valid_coordinates(col, row):
    return col in bps.CHESS_TO_GRID_COLUMNS and row in bps.CHESS_TO_GRID_ROWS


def validate_input(user_input, select_or_move):
    if len(user_input) is 0:
        return False, "Cancelled selection"
    elif len(user_input) is not INPUT_LENGTH:
        return False, bps.yellow("invalid input, one letter and one number required, ex: A1.\n") \
               + select_or_move

    col, row = user_input[0], user_input[1]

    if not valid_coordinates(col, row):
        return False, bps.yellow("Invalid coordinates: " +
                                str((col, row)) +
                                str(" A-H + 1-8 required\n")) + \
               select_or_move
    else:
        return True, ChessCoord(col, row)


def game_loop(pieces, selected_coord, moved_to_coords, piece_to_move):
    def select_piece(pieces, selected_coord, moved_to_coords, msg):
        dr.draw_board(pieces, selected_coord, moved_to_coords)

        if msg:
            print msg

        user_input = raw_input()
        user_input = user_input.upper()
        input_is_valid, input_result = validate_input(user_input, "Select piece")
        print "input_is_valid %s " % input_is_valid
        if not input_is_valid:
            select_piece(pieces, None, None, input_result)

        selected_coordinates = input_result
        print "selected_coordinates %s " % selected_coordinates
        piece_selection = filter(lambda piece: piece.chess_coord == selected_coordinates, pieces)

        if piece_selection:
            selected_piece = piece_selection[0]
            selected_coord = chess_coord_to_grid_coord(selected_piece.chess_coord)
            game_loop(pieces, selected_coord, None, selected_piece)

        else:
            select_piece(pieces, selected_coord, None, bps.yellow("no piece on that square\n") + "Select piece")

    def move_piece(pieces, selected_coord, moved_to_coord, piece_to_move, msg):
        dr.draw_board(pieces, selected_coord, moved_to_coord)

        if msg:
            print msg

        user_input = raw_input()
        user_input = user_input.upper()
        input_is_valid, input_result = validate_input(user_input, "Move piece ")
        if not input_is_valid:
            select_piece(pieces, None, None, input_result)

        new_coordinates = input_result
        move_inspect_result = piece_to_move.inspect_move(pieces, new_coordinates)

        if not move_inspect_result.is_valid_move and not move_inspect_result.was_blocked:
            move_piece(pieces, selected_coord, None, piece_to_move, "Invalid move for this piece")

        elif move_inspect_result.was_blocked:
                move_piece(pieces, None, None, piece_to_move, "another piece is blocking that move")
        else:
            if move_inspect_result.piece:
                pieces.remove(move_inspect_result.piece)

            piece_to_move.update_coords(new_coordinates )
            selected_coord = chess_coord_to_grid_coord(piece_to_move.chess_coord)
            moved_to_coord = chess_coord_to_grid_coord(new_coordinates)
            game_loop(pieces, selected_coord, moved_to_coord, None)

    if piece_to_move:
        move_piece(pieces, selected_coord, moved_to_coords, piece_to_move, "Move piece")
    else:
        select_piece(pieces, selected_coord, None, "Select piece")


starting_pieces = [
    # black pawns
    Pawn(ChessCoord('A', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('B', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('C', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('D', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('E', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('F', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('G', '7'), bps.black, dirs.go_south),
    Pawn(ChessCoord('H', '7'), bps.black, dirs.go_south),
    # black back row
    Rook(ChessCoord('A', '8'), bps.black),
    Knight(ChessCoord('B', '8'), bps.black),
    Bishop(ChessCoord('C', '8'), bps.black),
    Queen(ChessCoord('D', '8'), bps.black),
    King(ChessCoord('E', '8'), bps.black),
    Bishop(ChessCoord('F', '8'), bps.black),
    Knight(ChessCoord('G', '8'), bps.black),
    Rook(ChessCoord('H', '8'), bps.black),
    # white pawns
    Pawn(ChessCoord('A', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('B', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('C', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('D', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('E', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('F', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('G', '2'), bps.white, dirs.go_north),
    Pawn(ChessCoord('H', '2'), bps.white, dirs.go_north),
    # white back row
    Rook(ChessCoord('A', '1'), bps.white),
    Knight(ChessCoord('B', '1'), bps.white),
    Bishop(ChessCoord('C', '1'), bps.white),
    Queen(ChessCoord('D', '1'), bps.white),
    King(ChessCoord('E', '1'), bps.white),
    Bishop(ChessCoord('F', '1'), bps.white),
    Knight(ChessCoord('G', '1'), bps.white),
    Rook(ChessCoord('H', '1'), bps.white),
]

game_loop(starting_pieces, None, None, None)