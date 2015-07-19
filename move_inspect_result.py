import util

class MoveInspectResult:
    def __init__(self, is_valid_move, was_blocked, squares, possible_piece):
        self.is_valid_move = is_valid_move
        self.was_blocked = was_blocked
        self.squares = squares
        self.possible_piece = possible_piece

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
