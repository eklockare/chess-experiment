from all_square_coords import all_chess_coords
import random
from players.player import Player


class RandomPlayer(Player):
    def __init__(self, colour):
        Player.__init__(self, colour)

    def make_move(self, pieces, last_moved_piece_coord):
        print "%s's turn" % self.colour_name
        pieces_of_my_colour = filter(lambda piece: piece.colour == self.colour, pieces)

        pieces_moves_all_move_results = map(lambda piece:
                                            piece.inspect_moves_for_piece(
                                                pieces, all_chess_coords),
                                            pieces_of_my_colour)

        def get_piece_with_valid_moves(piece_moves_move_result):
            def gets_move_has_valid_move_results(move_move_result):
                move_result = move_move_result['move_result']
                return move_result.is_valid_move

            piece = piece_moves_move_result['piece']
            moves_move_result = piece_moves_move_result['moves_move_result']

            valid_moves_move_result = filter(gets_move_has_valid_move_results,
                                 moves_move_result)

            valid_moves = map(lambda move_move_result: move_move_result['move'],
                              valid_moves_move_result )
            if valid_moves:
                return piece, valid_moves
            else:
                return None

        pieces_moves_dirty = map(get_piece_with_valid_moves, pieces_moves_all_move_results)

        pieces_all_valid_moves = filter(lambda pm: pm is not None, pieces_moves_dirty)

        selected_piece, all_valid_moves = random.choice(pieces_all_valid_moves)

        move_to_make = random.choice(all_valid_moves)
        return selected_piece, move_to_make
