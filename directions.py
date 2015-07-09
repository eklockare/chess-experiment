import board_parts as bps
from board_parts import GridCoord


def is_within_board(col, row):
    if (0 <= row < 8) and (0 <= col < 8):
        return GridCoord(col, row)
    else:
        return None


def move_directions_knight():
    return [kn_go_north_east, kn_go_north_west, kn_go_east_north,
            kn_go_east_south, kn_go_south_east, kn_go_south_west,
            kn_go_west_south, kn_go_west_north]


def kn_go_north_east(grid_coord):
    return is_within_board(grid_coord.col + 1, grid_coord.row + 2)


def kn_go_north_west(grid_coord):
    return is_within_board(grid_coord.col - 1, grid_coord.row + 2)


def kn_go_east_north(grid_coord):
    return is_within_board(grid_coord.col + 2, grid_coord.row + 1)


def kn_go_east_south(grid_coord):
    return is_within_board(grid_coord.col + 2, grid_coord.row - 1)


def kn_go_south_east(grid_coord):
    return is_within_board(grid_coord.col + 1, grid_coord.row - 2)


def kn_go_south_west(grid_coord):
    return is_within_board(grid_coord.col - 1, grid_coord.row - 2)


def kn_go_west_south(grid_coord):
    return is_within_board(grid_coord.col - 2, grid_coord.row - 1)


def kn_go_west_north(grid_coord):
    return is_within_board(grid_coord.col - 2, grid_coord.row + 1)


def go_east(grid_coord):
    return is_within_board(grid_coord.col + 1, grid_coord.row)


def go_west(grid_coord):
    return is_within_board(grid_coord.col - 1, grid_coord.row)


def go_north(grid_coord):
    return is_within_board(grid_coord.col, grid_coord.row + 1)


def go_north_west(grid_coord):
    return is_within_board(grid_coord.col - 1, grid_coord.row + 1)


def go_north_east(grid_coord):
    return is_within_board(grid_coord.col + 1, grid_coord.row + 1)


def go_south(grid_coord):
    return is_within_board(grid_coord.col, grid_coord.row - 1)


def go_south_west(grid_coord):
    return is_within_board(grid_coord.col - 1, grid_coord.row - 1)


def go_south_east(grid_coord):
    return is_within_board(grid_coord.col + 1, grid_coord.row - 1)


def move_direction_pawn(color):
    if color is bps.white:
        return go_north
    else:
        return go_south


def move_directions_rook():
    return [go_north, go_west, go_south, go_east]


def move_directions_bishop():
    return [go_north_west, go_south_east, go_south_west, go_north_east]


def move_directions_queen():
    return move_directions_bishop() + move_directions_rook()

def is_diagonal_move(move_direction):
    return move_direction is go_north_east or \
           move_direction is go_north_west or \
           move_direction is go_south_east or \
           move_direction is go_south_west


def is_straight_move(move_direction):
    return move_direction is go_north or \
           move_direction is go_south or \
           move_direction is go_west or \
           move_direction is go_east

def get_direction(from_grid_coord, to_grid_coord):
    def is_northward_or_southward():
        if from_grid_coord.row < to_grid_coord.row:
           return go_north
        elif from_grid_coord.row > to_grid_coord.row:
            return go_south
        else:
            return None

    def is_westward_or_eastward():
        if from_grid_coord.col < to_grid_coord.col:
            return go_east
        elif from_grid_coord.col > to_grid_coord.col:
            return go_west
        else:
            return None

    north_or_south = is_northward_or_southward()
    west_or_east = is_westward_or_eastward()

    if not north_or_south:
        return west_or_east
    elif not west_or_east:
        return north_or_south
    elif north_or_south == go_north:
        if west_or_east == go_west:
            return go_north_west
        else:
            return go_north_east
    else:
        if west_or_east == go_west:
            return go_south_west
        else:
            return go_south_east
