import board_parts
import directions as dire

class Piece(object):
    def __init__(self, chess_coord, colour, letter, symbol, move_directions):
        self.move_directions = move_directions
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)
        self.colour = colour
        self.letter = letter
        self.symbol = symbol

    def is_valid_move(self, pieces, move):
        raise NotImplementedError("Please use subclass")

    def update_coords(self, chess_coord):
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)

    def get_direction_and_squares(self, move):
        return dire.get_move_direction_and_squares_in_between(self.grid_coord,
                                   board_parts.chess_coord_to_grid_coord(move),
                                   self.move_directions)

    def __str__(self):
        if self.colour == board_parts.black:
            color_name = "black"
        else:
            color_name = "white"

        return "%s %s, %s, %s" % \
               (self.letter,
                self.chess_coord,
                self.grid_coord,
                color_name)
