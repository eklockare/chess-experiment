import board_parts
from board_parts import GridCoord, ChessCoord, black, white, ROWS, COLUMNS

class Piece(object):
    def __init__(self, chess_coord, colour, letter, symbol):
        self.chess_coord = chess_coord
        self.grid_coord = GridCoord(COLUMNS[chess_coord.col],
                                                ROWS[chess_coord.row])
        self.colour = colour
        self.letter = letter
        self.symbol = symbol

    def is_valid_move(self, pieces, move):
        raise NotImplementedError("Please use subclass")

    def update_coords(self, chess_coord):
        self.chess_coord = chess_coord
        self.grid_coord = GridCoord(COLUMNS[chess_coord.col],
                                                ROWS[chess_coord.row])
