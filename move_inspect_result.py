import util

class MoveInspectResult:
    def __init__(self, is_valid_move, was_blocked, squares, possible_piece):
        self.is_valid_move = is_valid_move
        self.was_blocked = was_blocked
        self.squares = squares
        self.possible_piece = possible_piece
        self.was_castling_attempt = False  # TODO: ugly, will refactor

    def __str__(self):
        return "MoveInspectResult(%s, %s, %s, %s)" % (self.is_valid_move,
                                               self.was_blocked,
                                               map(str, self.squares),
                                               self.possible_piece)

    def __eq__(self, other):
        return self.is_valid_move == other.is_valid_move \
            and self.was_blocked == other.was_blocked \
            and self.possible_piece == other.possible_piece \
            and util.compare_lists(self.squares, other.squares)

class CastlingMoveInspectResult(MoveInspectResult):
    def __init__(self, is_valid_move, was_blocked, was_castling_attempt,
                 squares_in_between_threatened, castling_rook,
                 new_coord_rook):
        MoveInspectResult.__init__(self, is_valid_move, was_blocked, [], None)
        self.was_castling_attempt = was_castling_attempt
        self.squares_in_between_threatened = squares_in_between_threatened
        self.castling_rook = castling_rook
        self.new_coord_rook = new_coord_rook

    def __str__(self):
        return "CastlingMoveInspectResult(%s, %s, %s, %s, %s, %s)" % (self.is_valid_move,
                                                                  self.was_blocked,
                                                                  self.was_castling_attempt,
                                                                  self.squares_in_between_threatened,
                                                                  self.castling_rook,
                                                                  self.new_coord_rook
                                                                  )

    def __eq__(self, other):
        return self.is_valid_move == other.is_valid_move \
            and self.was_blocked == other.was_blocked \
            and self.possible_piece == other.possible_piece \
            and self.squares_in_between_threatened == other.squares_in_between_threatened\
            and util.compare_lists(self.squares, other.squares) \
            and self.castling_rook == other.castling_rook \
            and self.was_castling_attempt == other.was_castling_attempt \
            and self.new_coord_rook == other.new_coord_rook
