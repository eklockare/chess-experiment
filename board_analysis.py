




def analyze_threats_on_board(pieces, possible_taken_piece=None):
    pieces_without_possible_piece = filter(lambda piece: piece is not possible_taken_piece,
                                           pieces)
    if possible_taken_piece:
        possible_taken_piece.is_threat_to_these_pieces = []

    map(lambda piece:
        piece.add_possible_pieces_and_squares_to_threat_list(pieces_without_possible_piece),
        pieces_without_possible_piece)