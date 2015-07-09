import util

__author__ = 'erikk'


class MoveInspectResult:
    def __init__(self, is_valid_move, was_blocked, squares, piece):
        self.is_valid_move = is_valid_move
        self.was_blocked = was_blocked
        self.squares = squares
        self.piece = piece

    def __str__(self):
        return "MoveResult(%s, %s, %s, %s)" % (self.is_valid_move,
                                           self.was_blocked,
                                           map(str, self.squares),
                                           self.piece)

    def __eq__(self, other):
        return self.is_valid_move == other.is_valid_move \
               and self.was_blocked == other.was_blocked \
               and self.piece == other.piece \
               and util.compare_lists(self.squares, other.squares)