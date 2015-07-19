import board_parts
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
        self.is_threat_to_these_pieces = []

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

    def add_possible_pieces_to_threat_list(self, pieces):
        self.is_threat_to_these_pieces = []
        inspect_move_results = self.check_all_directions(pieces, self.grid_coord)

        inspect_move_results_with_possible_pieces = \
            filter(lambda inspect_move_result: inspect_move_result.possible_piece
                   is not None,
                   inspect_move_results)

        def add_possible_piece(possible_piece):
            if possible_piece.colour != self.colour:
                self.is_threat_to_these_pieces.append(possible_piece)

        map(lambda move_inspect_result: add_possible_piece(
            move_inspect_result.possible_piece),
            inspect_move_results_with_possible_pieces)

    def check_for_putting_self_in_check(self, pieces, new_coordinates, possible_piece):
        def detect_move_piece_king(piece):
            possible_own_king = filter(lambda threatened_piece: threatened_piece.letter == 'K'
                                       and threatened_piece.colour == self.colour,
                                       piece.is_threat_to_these_pieces)
            return len(possible_own_king) > 0

        self.analyze_threats_on_board_for_new_move(pieces,
                                                   new_coordinates,
                                                   possible_piece)
        own_king_checked = True in map(detect_move_piece_king, pieces)
        return own_king_checked

    def analyze_threats_on_board_for_new_move(self, pieces,
                                              new_coordinates,
                                              possible_piece=None):
        old_coords = self.chess_coord
        self.update_coords(new_coordinates)
        pieces_without_possible_piece = filter(lambda piece: piece is not possible_piece,
                                               pieces)
        if possible_piece:
            possible_piece.is_threat_to_these_pieces = []

        map(lambda piece:
            piece.add_possible_pieces_to_threat_list(pieces_without_possible_piece),
            pieces_without_possible_piece)

        self.update_coords(old_coords)

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
