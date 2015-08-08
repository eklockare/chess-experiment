import pprint
from all_square_coords import all_chess_coords
from board_analysis import analyze_threats_on_board
import util


def detect_if_king_is_mate(colour, pieces):
    possible_king = filter(lambda piece: piece.letter == 'K' and
                                         piece.colour == colour, pieces)
    if len(possible_king) == 0:
        return False

    analyze_threats_on_board(pieces)

    pieces_of_this_colour = filter(lambda piece: piece.colour == colour, pieces)

    piece_moves_all_move_results = map(lambda piece:
                                       piece.inspect_moves_for_piece(pieces, all_chess_coords),
                                       pieces_of_this_colour)

    def any_valid_move_available(piece, moves_move_results):
        def check_for_valid(move, move_result):
            return move_result.is_valid_move
        return map(lambda move_move_result:
                   check_for_valid(move_move_result['move'],
                                   move_move_result['move_result']),
                   moves_move_results)

    any_valid_move = map(lambda piece_moves_move_results:
            any_valid_move_available(piece_moves_move_results['piece'],
                                     piece_moves_move_results['moves_move_result']),
            piece_moves_all_move_results)

    any_valid_move_flat = util.flatten_list(any_valid_move)

    valid_move_exists = (True in any_valid_move_flat)

    return not valid_move_exists