# -*- coding: utf-8 -*-
class bcolors:
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

COLUMNS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
ROWS = {'8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, '1': 0}

IS_PIECE_ROW = True
IS_NOT_PIECE_ROW = False


class GridCoord(object):
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __eq__(self, other):
            return self.col == other.col and self.row == other.row


class ChessCoord(object):
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def __eq__(self, other):
        return self.col == other.col and self.row == other.row




def black(string):
    return bcolors.BLACK + string + bcolors.ENDC


def white(string):
    return bcolors.WHITE + string + bcolors.ENDC


def green(string):
    return bcolors.OKGREEN + string + bcolors.ENDC


def yellow(string):
    return bcolors.WARNING + string + bcolors.ENDC


def green_background(string):
    return bcolors.OKGREEN + string + bcolors.ENDC


def yellow_background(string):
    return bcolors.WARNING + string + bcolors.ENDC


def top_row():
    return [(top_letters, IS_NOT_PIECE_ROW), (h_separator_u, IS_NOT_PIECE_ROW), (v_separator, IS_NOT_PIECE_ROW),
            (v_separator, IS_PIECE_ROW),
            (h_separator_l, IS_NOT_PIECE_ROW)]


def middle_row():
    return [(v_separator, IS_NOT_PIECE_ROW), (v_separator, IS_PIECE_ROW), (h_separator_l, IS_NOT_PIECE_ROW)]
