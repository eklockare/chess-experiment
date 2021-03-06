from board_analysis import analyze_threats_on_board
import board_parts
from move_inspect_result import MoveInspectResult
from util import select_piece, flatten_list


class Piece(object):
    def __init__(self, chess_coord, colour, letter, symbol, move_directions):
        self.move_directions = move_directions
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)
        self.colour = colour
        self.letter = letter
        self.symbol = symbol
        self.is_threat_to_these_pieces = []
        self.is_threat_to_these_squares = []
        self.number_of_moves = 0

    def piece_is_enemy_king(self, piece):
        if piece is not None:
            return piece.letter == 'K' and piece.colour != self.colour
        else:
            return False

    def paths_and_piece_in_direction(self, from_coord, to_coord, pieces, direction, squares):
        new_coord_grid = direction(from_coord)
        if not new_coord_grid:
            return MoveInspectResult(False, False, squares, None)

        possible_piece = select_piece(new_coord_grid, pieces)
        if possible_piece and to_coord != new_coord_grid:
            return MoveInspectResult(False, True, squares, possible_piece)

        if self.piece_is_enemy_king(possible_piece):
            return MoveInspectResult(False, True, squares, possible_piece)

        squares.append(new_coord_grid)
        if to_coord == new_coord_grid:
            if possible_piece is not None and \
               possible_piece.colour == self.colour:
                return MoveInspectResult(False, True, squares, possible_piece)
            else:
                return MoveInspectResult(True, False, squares, possible_piece)
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
            move_inspect_result = positive_result[0]
            move_inspect_result.will_put_self_in_check = \
                self.check_for_putting_self_in_check(pieces,
                                                     move,
                                                     move_inspect_result)
            move_inspect_result.is_valid_move = move_inspect_result.is_valid_move and \
                not move_inspect_result.will_put_self_in_check

            return move_inspect_result
        else:
            blocked_result = filter(lambda move_inspect_result:
                                    move_inspect_result.was_blocked,
                                    inspect_move_results)
            if blocked_result:
                return blocked_result[0]
            else:
                return MoveInspectResult(False, False, [], None)

    def update_coord(self, chess_coord):
        self.number_of_moves += 1
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)

    def dry_run_update_coord(self, chess_coord):
        self.chess_coord = chess_coord
        self.grid_coord = board_parts.chess_coord_to_grid_coord(chess_coord)

    def add_all_squares_from_inspect_move_results_to_threat_list(self, inspect_move_results):
        all_squares = map(lambda imr: imr.squares, inspect_move_results)
        for squares in all_squares:
            for square in squares:
                self.is_threat_to_these_squares.append(square)

    def add_possible_pieces_and_squares_to_threat_list(self, pieces):
        self.is_threat_to_these_pieces = []
        self.is_threat_to_these_squares = []
        inspect_move_results = self.check_all_directions(pieces, self.grid_coord)

        inspect_move_results_with_possible_pieces = \
            filter(lambda inspect_move_result: inspect_move_result.possible_piece
                   is not None,
                   inspect_move_results)
        self.add_all_squares_from_inspect_move_results_to_threat_list(inspect_move_results)

        def add_possible_piece(possible_piece):
            if possible_piece.colour != self.colour:
                self.is_threat_to_these_pieces.append(possible_piece)

        map(lambda move_inspect_result: add_possible_piece(
            move_inspect_result.possible_piece),
            inspect_move_results_with_possible_pieces)

    def check_for_putting_self_in_check(self, pieces, new_coordinates, move_inspect_result):
        self.analyze_threats_on_board_for_new_move(pieces,
                                                   new_coordinates,
                                                   move_inspect_result.possible_piece)
        return self.check_if_own_king_in_check(pieces)

    def check_if_own_king_in_check(self, pieces):
        def detect_move_piece_king(piece):
            possible_own_king = filter(lambda threatened_piece: threatened_piece.letter == 'K'
                                       and threatened_piece.colour == self.colour,
                                       piece.is_threat_to_these_pieces)
            return len(possible_own_king) > 0
        own_king_checked = True in map(detect_move_piece_king, pieces)
        return own_king_checked

    def analyze_threats_on_board_for_new_move(self, pieces,
                                              new_coordinates,
                                              possible_piece=None):
        old_coord = self.chess_coord
        self.dry_run_update_coord(new_coordinates)
        analyze_threats_on_board(pieces, possible_piece)

        self.dry_run_update_coord(old_coord)

    def get_all_squares_the_enemy_threatens(self, pieces):
        enemy_pieces = filter(lambda piece: piece.colour != self.colour, pieces)
        squares_unflattened = map(lambda piece: piece.is_threat_to_these_squares,
                                  enemy_pieces)
        return flatten_list(squares_unflattened)

    def inspect_moves_for_piece(self, pieces, moves):
        return {'piece': self,
                'moves_move_result':
                    map(lambda move: {'move': move,
                                      'move_result': self.inspect_move(pieces, move)
                                      }, moves)}

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
