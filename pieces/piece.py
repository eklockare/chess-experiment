import board_parts
import directions as dire
from move_inspect_result import MoveInspectResult


def find_possible_piece(pieces, grid_coord):
        possible_piece = filter(lambda piece: piece.grid_coord == grid_coord, pieces)
        if possible_piece:
            return possible_piece[0]
        else:
            return None

class Piece(object):
    def __init__(self, chess_coord, colour, letter, symbol, move_directions):
        self.move_directions = move_directions
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)
        self.colour = colour
        self.letter = letter
        self.symbol = symbol

    def paths_and_piece_in_direction(self, from_coord, to_coord, pieces, direction, squares):
        new_coord_grid = direction(from_coord)
        if not new_coord_grid:
            return MoveInspectResult(False, False, squares, None)

        squares.append(new_coord_grid)

        possible_piece = find_possible_piece(pieces, new_coord_grid)
        if to_coord == new_coord_grid:
            if possible_piece:
                if possible_piece.colour == self.colour:
                    return MoveInspectResult(False, True, squares, possible_piece)
                else:
                    return MoveInspectResult(True, False, squares, possible_piece)
            else:
                return MoveInspectResult(True, False, squares, None)

        elif possible_piece:
            return MoveInspectResult(False, True, squares, possible_piece)
        else:
            return self.paths_and_piece_in_direction(new_coord_grid, to_coord, pieces, direction, squares)

    def check_all_directions(self, pieces, move_to):
        possible_moves = map(lambda direction:
                             self.paths_and_piece_in_direction(
                                 self.grid_coord,
                                 move_to,
                                 pieces,
                                 direction,
                                 []),
                             self.move_directions)
        return possible_moves

    def inspect_move(self, pieces, move):
        move_grid = board_parts.chess_coord_to_grid_coord(move)
        inspect_move_results = self.check_all_directions(pieces, move_grid)
        positive_result = filter(lambda move_inspect_result:
                                 move_inspect_result.is_valid_move,
                       inspect_move_results)
        if positive_result:
            return positive_result[0]
        else:
            blocked_result = filter(lambda move_inspect_result:
                                    move_inspect_result.was_blocked,
                       inspect_move_results)
            if blocked_result:
                return blocked_result[0]
            else:
                return MoveInspectResult(False, False, [], None)

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
