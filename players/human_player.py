
from board_parts import CHESS_TO_GRID_COLUMNS, CHESS_TO_GRID_ROWS, yellow, ChessCoord
from drawing import draw_board

INPUT_LENGTH = 2

def valid_coordinates(col, row):
    return col in CHESS_TO_GRID_COLUMNS and row in CHESS_TO_GRID_ROWS


def validate_input(user_input, select_or_move):
    if len(user_input) is 0:
        return None, "Cancelled selection"
    elif len(user_input) is not INPUT_LENGTH:
        return None, yellow("invalid input, one letter and one number required, ex: A1.\n") \
            + select_or_move

    col, row = user_input[0], user_input[1]

    if not valid_coordinates(col, row):
        return None, yellow("Invalid coordinates: " +
                             str((col, row)) +
                             str(" A-H + 1-8 required\n")) + select_or_move
    else:
        return ChessCoord(col, row), None


class HumanPlayer:
    def __init__(self, colour):
        self.colour = colour

    def get_player_input(self, pieces):
        user_input = raw_input()
        user_input = user_input.upper()
        input_coord, msg = validate_input(user_input, "Select piece")

        if input_coord is None:
            print msg
            return self.get_player_input(pieces)
        else:
            return input_coord

    def select_piece(self, pieces):
        print "Select a piece"
        selected_coordinates = self.get_player_input(pieces)
        piece_selection = filter(lambda piece: piece.chess_coord == selected_coordinates, pieces)

        if len(piece_selection) > 0:
            selected_piece = piece_selection[0]
            if selected_piece.colour != self.colour:
                print yellow("That is not your piece")
                return self.select_piece(pieces)
        else:
            print yellow("No piece on that square")
            return self.select_piece(pieces)

        return selected_piece

    def make_move(self, pieces, piece_to_move):
        print "Move the selected piece"
        new_coordinates = self.get_player_input(pieces)
        move_inspect_result = piece_to_move.inspect_move(pieces, new_coordinates)

        if not move_inspect_result.is_valid_move and not move_inspect_result.was_blocked:
            if move_inspect_result.will_put_self_in_check:
                print "Check!"
                return self.make_move(pieces, piece_to_move)
            else:
                print "Invalid move for this piece"
                return self.make_move(pieces, piece_to_move)

        elif move_inspect_result.was_blocked:
            print "Another piece is blocking that move"
            return self.make_move(pieces, piece_to_move)

        return new_coordinates
