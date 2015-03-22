# -*- coding: utf-8 -*-
import board_parts as bps
import drawing as dr
import movement as mov
import collision as coll
from board_parts import ChessCoor
from board_parts import GridCoor
from board_parts import Piece

INPUT_LENGTH = 2


def convert_last_move(col, row, col_to=None, row_to=None):
    if row_to:
        return bps.ROWS[row], bps.COLUMNS[col], bps.ROWS[row_to], bps.COLUMNS[col_to]
    else:
        return bps.ROWS[row], bps.COLUMNS[col], None, None


#def convert_coordinates(piece):
#    chess_coors, colour, letter, symbol = piece
#    return GridCoor(bps.ROWS[chess_coors.row], bps.COLUMNS[chess_coors.col]), colour, symbol


def valid_coordinates(col, row):
    return col in bps.COLUMNS and row in bps.ROWS


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
    # converted_coordinates_pieces = map(convert_coordinates, pieces)

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

        piece_selection = filter(lambda piece: piece.chess_coor.col is col and piece.chess_coor.row is row, pieces)

        if piece_selection:
            selected_piece = piece_selection[0]
            #piece_col, piece_row, color, letter, symbol = selected_piece


            last_move = convert_last_move(selected_piece.chess_coor.col, selected_piece.chess_coor.row)
            game_loop(pieces, last_move, selected_piece)

        else:
            select_piece(pieces, last_move, bps.yellow("no piece on that square\n") + "Select piece")

    def move_piece(pieces, last_move, msg):
        dr.draw_board(pieces, last_move)

        if msg:
            print msg

        #col_old, row_old, color, letter, symbol = piece_to_move
        color = piece_to_move.colour
        letter = piece_to_move.letter
        symbol = piece_to_move.symbol
        col_old = piece_to_move.chess_coor.col
        row_old = piece_to_move.chess_coor.row

        user_input = raw_input()
        user_input = user_input.upper()
        input_result = validate_input(user_input, "Move piece ")
        col_new, row_new = input_result

        if not col_new:
            if row_new is 'cancel':
                select_piece(pieces, None, "cancelled")
            else:
                _, msg = input_result
                move_piece(pieces, last_move, msg)

        # check if move is valid here
        # is valid for this piece
        is_valid_movement, possible_moves = mov.is_valid_movement_pattern_for_piece(piece_to_move, col_new,
                                                                                    row_new, pieces)

        print "is_valid_movement, possible_moves : " + str(is_valid_movement) + "  " + str(possible_moves)

        if not is_valid_movement:
            move_piece(pieces, last_move, "Invalid move for this piece")
        else:
            # check if there is a piece on moved to square, if so remove it


            # puts us in check
            # pieces.remove(piece_to_move)
            # moved_piece = (col_new, row_new, color, letter, symbol)
            print "col_new, row_new: " +str((col_new, row_new))
            # piece_to_move.
            # pieces.append(moved_piece)
            piece_to_move.update_coors(ChessCoor(col_new, row_new))

            last_move = convert_last_move(col_old, row_old, col_new, row_new)
            game_loop(pieces, last_move, None)

    if piece_to_move:
        move_piece(pieces, last_move, "Move piece")
    else:
        select_piece(pieces, last_move, "Select piece")


starting_pieces = [
    # black pawns
    Piece(ChessCoor('A', '7'), bps.black, 'P', '♟'), Piece(ChessCoor('B', '7'), bps.black, 'P', '♟'),
    Piece(ChessCoor('C', '7'), bps.black, 'P', '♟'), Piece(ChessCoor('D', '7'), bps.black, 'P', '♟'),
    Piece(ChessCoor('E', '7'), bps.black, 'P', '♟'), Piece(ChessCoor('F', '7'), bps.black, 'P', '♟'),
    Piece(ChessCoor('G', '7'), bps.black, 'P', '♟'), Piece(ChessCoor('H', '7'), bps.black, 'P', '♟'),
    # black back row
    Piece(ChessCoor('A', '8'), bps.black, 'R', '♜'), Piece(ChessCoor('B', '8'), bps.black, 'Kn', '♞'),
    Piece(ChessCoor('C', '8'), bps.black, 'B', '♝'), Piece(ChessCoor('D', '8'), bps.black, 'Q', '♛'),
    Piece(ChessCoor('E', '8'), bps.black, 'K', '♚'), Piece(ChessCoor('F', '8'), bps.black, 'B', '♝'),
    Piece(ChessCoor('G', '8'), bps.black, 'Kn', '♞'), Piece(ChessCoor('H', '8'), bps.black, 'R', '♜'),
    # white pawns
    Piece(ChessCoor('A', '2'), bps.white, 'P', '♙'), Piece(ChessCoor('B', '2'), bps.white, 'P', '♙'),
    Piece(ChessCoor('C', '2'), bps.white, 'P', '♙'), Piece(ChessCoor('D', '2'), bps.white, 'P', '♙'),
    Piece(ChessCoor('E', '2'), bps.white, 'P', '♙'), Piece(ChessCoor('F', '2'), bps.white, 'P', '♙'),
    Piece(ChessCoor('G', '2'), bps.white, 'P', '♙'), Piece(ChessCoor('H', '2'), bps.white, 'P', '♙'),
    # white back row
    Piece(ChessCoor('A', '1'), bps.white, 'R', '♖'), Piece(ChessCoor('B', '1'), bps.white, 'Kn', '♘'),
    Piece(ChessCoor('C', '1'), bps.white, 'B', '♗'), Piece(ChessCoor('D', '1'), bps.white, 'Q', '♕'),
    Piece(ChessCoor('E', '1'), bps.white, 'K', '♔'), Piece(ChessCoor('F', '1'), bps.white, 'B', '♗'),
    Piece(ChessCoor('G', '1'), bps.white, 'Kn', '♘'), Piece(ChessCoor('H', '1'), bps.white, 'R', '♖'),
]
game_loop(starting_pieces, None, None)