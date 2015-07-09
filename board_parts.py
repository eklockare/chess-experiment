# -*- coding: utf-8 -*-
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
BLACK = '\033[90m'
WHITE = '\033[97m'
GREEN_BACKGROUND = '\033[42m'
YELLOW_BACKGROUND = '\033[43m'

top_letters = ['  A   ', '  B   ', '  C   ', '  D   ', '  E   ', '  F   ', '  G   ', '  H   ']
h_separator_u = ['______', '______', '______', '______', '______', '______', '______', '______']
h_separator_l = ['|_____|', '|_____|', '|_____|', '|_____|', '|_____|', '|_____|', '|_____|', '|_____|']
v_separator = ['|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |', '|     |']

NUM_ROWS = range(0, 8)
NUM_COLS = range(0, 8)


def inverse_dict(dictionary):
    return dict((v, k) for k, v in dictionary.iteritems())


CHESS_TO_GRID_COLUMNS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
CHESS_TO_GRID_ROWS = {'8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, '1': 0}

GRID_TO_CHESS_COLUMNS = inverse_dict(CHESS_TO_GRID_COLUMNS)
GRID_TO_CHESS_ROWS = inverse_dict(CHESS_TO_GRID_ROWS)

IS_PIECE_ROW = True
IS_NOT_PIECE_ROW = False


def grid_coord_to_chess_coord(grid_coord):
    return GridCoord(GRID_TO_CHESS_COLUMNS[grid_coord.col], GRID_TO_CHESS_ROWS[grid_coord.row])


def chess_coord_to_grid_coord(chess_coord):
    return GridCoord(CHESS_TO_GRID_COLUMNS[chess_coord.col], CHESS_TO_GRID_ROWS[chess_coord.row])


class GridCoord(object):
    def __init__(self, col, row):
        assert (type(col) is int and type(row) is int)
        assert (col in NUM_COLS and row in NUM_ROWS)
        self.col = col
        self.row = row

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    def __ne__(self, other):
        return self.col != other.col or self.row != other.row

    def __str__(self):
        return "GridCoord(%s, %s)" % (self.col, self.row)


class ChessCoord(object):
    def __init__(self, col, row):
        assert (type(col) is str and type(row) is str)
        self.col = col
        self.row = row

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row

    def __ne__(self, other):
        return self.col != other.col or self.row != other.row

    def __str__(self):
        return "ChessCoord(%s, %s)" % (self.col, self.row)


def black(string):
    return BLACK + string + ENDC


def white(string):
    return WHITE + string + ENDC


def green(string):
    return OKGREEN + string + ENDC


def yellow(string):
    return WARNING + string + ENDC


def green_background(string):
    return OKGREEN + string + ENDC


def yellow_background(string):
    return WARNING + string + ENDC


def top_row():
    return [(top_letters, IS_NOT_PIECE_ROW), (h_separator_u, IS_NOT_PIECE_ROW), (v_separator, IS_NOT_PIECE_ROW),
            (v_separator, IS_PIECE_ROW),
            (h_separator_l, IS_NOT_PIECE_ROW)]


def middle_row():
    return [(v_separator, IS_NOT_PIECE_ROW), (v_separator, IS_PIECE_ROW), (h_separator_l, IS_NOT_PIECE_ROW)]
