from all_square_coords import all_chess_coords
import random

class RandomPlayer:
    def __init__(self, colour):
        self.colour = colour
        self.move_to_make = None

    def select_piece(self, pieces):
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

        # print "pieces_all_valid_moves %s " % map(str, pieces_all_valid_moves)

        selected_piece, all_valid_moves = random.choice(pieces_all_valid_moves)

        self.move_to_make = random.choice(all_valid_moves)

        print "selected_piece %s, \n selected move %s " % (selected_piece, self.move_to_make)

        return selected_piece

    def make_move(self, pieces, piece_to_move):
        return self.move_to_make
