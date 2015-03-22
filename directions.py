import board_parts as bps


def is_within_board(col, row):
    print "is_within_board: " + str(col) + " " + str(row)
    if (0 <= row < 8) and (0 <= col < 8):
        return row, col
    else:
        return None, None

def move_directions_knight():
    return [kn_go_north_east, kn_go_north_west, kn_go_east_north,
            kn_go_east_south, kn_go_south_east, kn_go_south_west,
            kn_go_west_south, kn_go_west_north]

def kn_go_north_east(col_num, row_num):
    return is_within_board(col_num - 2, row_num + 1)

def kn_go_north_west(col_num, row_num):
    return is_within_board(col_num - 2, row_num - 1)

def kn_go_east_north(col_num, row_num):
    return is_within_board(col_num - 1, row_num + 2)

def kn_go_east_south(col_num, row_num):
    return is_within_board(col_num + 1, row_num + 2)

def kn_go_south_east(col_num, row_num):
    return is_within_board(col_num + 2, row_num + 1)

def kn_go_south_west(col_num, row_num):
    return is_within_board(col_num + 2, row_num - 1)

def kn_go_west_south(col_num, row_num):
    return is_within_board(col_num + 1, row_num - 2)

def kn_go_west_north(col_num, row_num):
    return is_within_board(col_num - 1, row_num - 2)

def go_east(col_num, row_num):
    return is_within_board(col_num, row_num + 1)


def go_west(col_num, row_num):
    return is_within_board(col_num, row_num - 1)


def go_north(col_num, row_num):
    print " !! col_num, row_num " + str((col_num, row_num)) + "is_within_board: " + str(is_within_board(col_num, row_num - 1))
    return is_within_board(col_num, row_num - 1)


def go_north_west(col_num, row_num):
    return is_within_board(col_num - 1, row_num - 1)


def go_north_east(col_num, row_num):
    return is_within_board(col_num + 1, row_num - 1)


def go_south(col_num, row_num):
    return is_within_board(col_num + 1, row_num)


def go_south_west(col_num, row_num):
    return is_within_board(col_num + 1, row_num - 1)


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

