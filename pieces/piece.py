import board_parts
import directions as dire
from directions import DirectionResult
from movement import MoveResult


class Piece(object):
    def __init__(self, chess_coord, colour, letter, symbol, move_directions):
        self.move_directions = move_directions
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)
        self.colour = colour
        self.letter = letter
        self.symbol = symbol

    def find_possible_piece(self, pieces, grid_coord):
        possible_piece = filter(lambda piece: piece.grid_coord == grid_coord, pieces)
        if possible_piece:
            return possible_piece[0]
        else:
            return None

    def paths_and_piece_in_direction(self, from_coord, pieces, direction, squares):
        new_coord_grid = direction(from_coord)
        if not new_coord_grid:
            return DirectionResult(squares, None)

        possible_piece = self.find_possible_piece(pieces, new_coord_grid)

        if possible_piece:
            return DirectionResult(squares, possible_piece)
        else:
            squares.append(new_coord_grid)
            return self.paths_and_piece_in_direction(new_coord_grid, pieces, direction, squares)

    def check_all_directions(self, pieces):
        possible_moves = map(lambda direction:
                             self.paths_and_piece_in_direction(self.grid_coord, pieces, direction, []),
                             self.move_directions)
        return possible_moves

    def is_valid_move(self, pieces, move):
        move_grid = board_parts.chess_coord_to_grid_coord(move)
        direction_results = self.check_all_directions(pieces)

        match = filter(lambda direction_result: move_grid in
                       direction_result.squares,
                       direction_results)
        if match:
            return MoveResult(len(match) == 1, match[0])
        else:
            return MoveResult(False, None)

    def update_coords(self, chess_coord):
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)

    def get_direction_and_squares(self, grid_move):
        return dire.get_move_direction_and_squares_in_between(self.grid_coord,
                                   grid_move,
                                   self.move_directions)

    def __str__(self):
        if self.colour == board_parts.black:
            color_name = "black"
        else:
            color_name = "white"

        return "Piece(%s, %s, %s, %s)" % \
               (self.letter,
                self.chess_coord,
                self.grid_coord,
                color_name)
