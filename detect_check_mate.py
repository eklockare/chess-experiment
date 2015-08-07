import pprint
from all_square_coords import all_chess_coords
from board_analysis import analyze_threats_on_board
import util


def detect_if_king_is_mate(colour, pieces):
    possible_king = filter(lambda piece: piece.letter == 'K' and
                                         piece.colour == colour, pieces)
    if len(possible_king) == 0:
        return False

    own_king = possible_king[0]

    analyze_threats_on_board(pieces)
    in_check = own_king.check_if_own_king_in_check(pieces)

    if not in_check:
        return False

    pieces_of_this_colour = filter(lambda piece: piece.colour == colour, pieces)

    piece_moves_all_move_results = map(lambda piece:
                                       piece.inspect_moves_for_piece(pieces, all_chess_coords),
                                       pieces_of_this_colour)

    def valid_and_not_putting_in_check(piece, moves_move_results):
        def check_move_for_check(move, move_result):
            return move_result.is_valid_move \
                   and not piece.check_for_putting_self_in_check(pieces,
                                                                 move,
                                                                 move_result)

        return map(lambda move_move_result:
                   check_move_for_check(move_move_result['move'],
                                        move_move_result['move_result']),
                   moves_move_results)

    valid_moves_that_blocks_check = \
        map(lambda piece_moves_move_results:
            valid_and_not_putting_in_check(piece_moves_move_results['piece'],
                                           piece_moves_move_results['moves_move_result']),
            piece_moves_all_move_results)

    move_results_puts_in_check_flatten = util.flatten_list(valid_moves_that_blocks_check)

    return not (True in move_results_puts_in_check_flatten)
