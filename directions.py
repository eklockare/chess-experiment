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


def get_move_direction_and_squares_in_between(grid_coord_from, grid_coord_to, directions):
    def go_until_hit_or_outside(grid_coord_from, grid_coord_to, direction, squares_in_between):
        grid_coord_move = direction(grid_coord_from)

        if grid_coord_move is not None:
            if grid_coord_from == grid_coord_to:
                return direction, squares_in_between
            else:
                squares_in_between.append(grid_coord_move)
                return go_until_hit_or_outside(grid_coord_move, grid_coord_to, direction, squares_in_between)
        else:
            return None, None

    tried_directions = map(lambda direction: go_until_hit_or_outside(grid_coord_from, grid_coord_to, direction, []),
                           directions)
    found_direction = filter(lambda direction_squares: direction_squares[0], tried_directions)

    if found_direction:
        return True, found_direction[0][0], found_direction[0][1]
    else:
        return False, None, None


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
