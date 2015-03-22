import board_parts as bps
import directions as dirs




def convert_from_chess_coor_to_grid(col, row):
    return bps.ROWS[row], bps.COLUMNS[col]


def flatten_list(list):
    return [item for sublist in list for item in sublist]


def go_max_distances(moves, move_direction, pieces, from_col, from_row, moves_left=None):
    print " 66 from_row, from_col: " + str((from_col, from_row))

    new_row, new_col = move_direction(from_col, from_row)

    # check here if piece is blocking
    print " %% new_row, new_col: " + str((new_col, new_row))


    if new_row is not None and moves_left is None:
        moves.append((new_col, new_row))
        return go_max_distances(moves, move_direction, pieces, new_col, new_row, None)
    elif new_row is not None and moves_left > 0:
        moves.append((new_col, new_row))
        return go_max_distances(moves, move_direction, pieces, new_col, new_row, moves_left - 1)
    else:
        return moves


def pawn_is_on_start_row(row, color):
    return color is bps.black and row is 1 or color is bps.white and row is 6


def move_pawn(move_direction, pieces, col_num, row_num, color):
    print " && move_pawn " + str((col_num, row_num))
    if pawn_is_on_start_row(row_num, color):
        print "is on start row"
        go_max = go_max_distances([], move_direction, pieces, col_num, row_num, moves_left=2)
        print "go_max: " + str(go_max)
        return go_max
    else:
        go_max = go_max_distances([], move_direction, pieces, col_num, row_num, moves_left=1)
        print "go_max: " + str(go_max)
        return go_max


def move_piece(move_directions, pieces, col_num, row_num, max_moves=None):
    return flatten_list(map(lambda move_direction:
                            go_max_distances([], move_direction, pieces, col_num, row_num, max_moves),
                            move_directions))


def possible_moves_for_piece(piece, pieces):
    #col, row, color, letter, symbol = piece
    color = piece.colour
    letter = piece.letter
    symbol = piece.symbol
    col_num, row_num = piece.grid_coor.col, piece.grid_coor.row
    print "possible_moves_for_piece: " + str((col_num, row_num))
    # convert_from_chess_coor_to_grid(col, row)

    #col, row = piece.chess_coor.col, piece.chess_coor.row

    if letter is 'P':
        move_direction = dirs.move_direction_pawn(color)
        print " ## row_num, col_num: " + str((col_num, row_num)) + " move_direction: " + str(move_direction)
        return move_pawn(move_direction, pieces, col_num, row_num, color)
    elif letter is 'R':
        move_directions = dirs.move_directions_rook()
        return move_piece(move_directions, pieces, col_num, row_num)
    elif letter is 'B':
        move_directions = dirs.move_directions_bishop()
        return move_piece(move_directions, pieces, col_num, row_num)
    elif letter is 'Q':
        move_directions = dirs.move_directions_queen()
        return move_piece(move_directions, pieces, col_num, row_num)
    elif letter is 'K':
        move_directions = dirs.move_directions_queen()
        return move_piece(move_directions, pieces, col_num, row_num, max_moves=1)
    elif letter is 'Kn':
        move_directions = dirs.move_directions_knight()
        return move_piece(move_directions, pieces, col_num, row_num)


def is_valid_movement_pattern_for_piece(piece, to_col, to_row, pieces):
    print " to_col, to_row: " + str((to_col, to_row))

    print "is valid for piece: " + str(piece.letter) + "  " + str(piece.chess_coor.col) + "  " + \
        str(piece.chess_coor.row) + "  " + str(piece.grid_coor.row) + "  " + str(piece.grid_coor.col)

    to_grid_row, to_grid_col = convert_from_chess_coor_to_grid(to_col, to_row)

    print " $$ to_grid_col, to_grid_row: " + str((to_grid_col, to_grid_row))

    possible_moves = possible_moves_for_piece(piece, pieces)

    move_is_possible = (to_grid_col, to_grid_row) in possible_moves

    print "(to_col, to_row): " + str((to_grid_col, to_grid_row))
    print "possible_moves : " + str(possible_moves)
    print "move_is_possible : " + str(move_is_possible)

    return move_is_possible, possible_moves



