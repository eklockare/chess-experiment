
from board_parts import CHESS_TO_GRID_COLUMNS, CHESS_TO_GRID_ROWS, yellow, ChessCoord, grid_coord_to_chess_coord, \
    chess_coord_to_grid_coord
from drawing import draw_board
from players.player import Player

INPUT_LENGTH = 2

def valid_coordinates(col, row):
    return col in CHESS_TO_GRID_COLUMNS and row in CHESS_TO_GRID_ROWS

VALID = 0
CANCELLED = 1
INVALID_INPUT = 2
INVALID_COORDINATES = 3

def validate_input(user_input, select_or_move):
    if len(user_input) is 0:
        return CANCELLED, None, None
    elif len(user_input) is not INPUT_LENGTH:
        return INVALID_INPUT, None, \
               yellow("Invalid input, one letter and one number required, ex: A1.\n") \
               + select_or_move

    col, row = user_input[0], user_input[1]

    if not valid_coordinates(col, row):
        return INVALID_COORDINATES, None, yellow("Invalid coordinates: " +
                             str((col, row)) +
                             str(" A-H + 1-8 required\n")) + select_or_move
    else:
        return VALID, ChessCoord(col, row), None


class HumanPlayer(Player):
    def __init__(self, colour):
        Player.__init__(self, colour)

    def get_player_input(self, pieces):
        user_input = raw_input()
        user_input = user_input.upper()
        result, input_coord, msg = validate_input(user_input, "Select piece")

        if result is VALID:
            return VALID, input_coord
        elif result is CANCELLED:
            return CANCELLED, None
        else:
            print msg
            return self.get_player_input(pieces)

    def make_move(self, pieces, last_moved_piece_coord):
        result = -1
        while result is not VALID:
            print "%s's turn" % self.colour_name
            print "Select a piece"
            result, selected_coordinates = self.get_player_input(pieces)
            if result is VALID:
                selected_coordinates_grid = chess_coord_to_grid_coord(selected_coordinates)
                draw_board(pieces, selected_coordinates_grid, last_moved_piece_coord)
            else:
                print "Cancelled"
                draw_board(pieces, None, last_moved_piece_coord)

        piece_selection = filter(lambda piece: piece.chess_coord == selected_coordinates, pieces)

        if len(piece_selection) > 0:
            selected_piece = piece_selection[0]
            if selected_piece.colour != self.colour:
                print yellow("That is not your piece")
                return self.make_move(pieces, last_moved_piece_coord)
        else:
            print yellow("No piece on that square")
            return self.make_move(pieces, last_moved_piece_coord)

        result = -1
        while result is not VALID:
            print "%s's turn" % self.colour_name
            print "Move the selected piece"
            result, new_coordinates = self.get_player_input(pieces)
#            if result is VALID:
#                draw_board(pieces, selected_coordinates_grid, last_moved_piece_coord)
            if result is CANCELLED:
                print "Cancelled"
                draw_board(pieces, None, last_moved_piece_coord)
                return self.make_move(pieces, last_moved_piece_coord)

        print "human new_coordinates %s" % new_coordinates
        move_inspect_result = selected_piece.inspect_move(pieces, new_coordinates)

        if not move_inspect_result.is_valid_move and not move_inspect_result.was_blocked:
            if move_inspect_result.will_put_self_in_check:
                print "Check!"
                return self.make_move(pieces, last_moved_piece_coord)
            else:
                print "Invalid move for this piece"
                return self.make_move(pieces, last_moved_piece_coord)

        elif move_inspect_result.was_blocked:
            print "Another piece is blocking that move"
            return self.make_move(pieces, last_moved_piece_coord)

        return selected_piece, new_coordinates
