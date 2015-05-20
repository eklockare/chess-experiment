import board_parts as bps
from board_parts import GridCoord

def is_within_board(col, row):
    if (0 <= row < 8) and (0 <= col < 8):
        return col, row
    else:
        print "is within board col %s row %s" % (col, row)
        return None, None


def move_directions_knight():
    return [kn_go_north_east, kn_go_north_west, kn_go_east_north,
            kn_go_east_south, kn_go_south_east, kn_go_south_west,
            kn_go_west_south, kn_go_west_north]


def kn_go_north_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num - 2)


def kn_go_north_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num - 2)


def kn_go_east_north(col_num, row_num):
    return is_within_board(col_num + 2, row_num - 1)


def kn_go_east_south(col_num, row_num):
    return is_within_board(col_num + 2, row_num + 1)


def kn_go_south_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num + 2)


def kn_go_south_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num + 2)


def kn_go_west_south(col_num, row_num):
    return is_within_board(col_num - 2, row_num + 1)


def kn_go_west_north(col_num, row_num):
    return is_within_board(col_num - 2, row_num - 1)


def go_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num)


def go_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num)


def go_north(col_num, row_num):
    return is_within_board(col_num, row_num - 1)


def go_north_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num - 1)


def go_north_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num - 1)


def go_south(col_num, row_num):
    return is_within_board(col_num, row_num + 1)


def go_south_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num + 1)


def go_south_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num + 1)


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
        col_move, row_move = direction(grid_coord_from.col, grid_coord_from.row)

        if col_move is not None and row_move is not None:
            if col_move is grid_coord_to.col and row_move is grid_coord_to.row:
                return direction, squares_in_between
            else:
                move = GridCoord(col_move, row_move)
                squares_in_between.append(move)
                return go_until_hit_or_outside(move, grid_coord_to, direction, squares_in_between)
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
