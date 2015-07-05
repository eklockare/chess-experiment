from board_parts import GridCoord, chess_coord_to_grid_coord, ChessCoord, black, white
import directions as dirs
import util


def go_max_distances(moves, move_direction, pieces, from_col, from_row, moves_left=None):
    print " 66 from_row, from_col: " + str((from_col, from_row))

    new_coord = move_direction(GridCoord(from_col, from_row))

    # check here if piece is blocking
    print " %% new_row, new_col: " + str(new_coord)

    if new_coord is not None and moves_left is None:
        moves.append(new_coord)
        return go_max_distances(moves, move_direction, pieces,
                                new_coord.col, new_coord.row, None)
    elif new_coord is not None and moves_left > 0:
        moves.append(new_coord)
        return go_max_distances(moves, move_direction, pieces, new_coord.col,
                                new_coord.row, moves_left - 1)
    else:
        return moves


def pawn_is_on_start_row(row, color):
    return color is black and row is 1 or color is white and row is 6


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
    return util.flatten_list(map(lambda move_direction:
                            go_max_distances([], move_direction, pieces, col_num, row_num, max_moves),
                            move_directions))


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

def possible_moves_for_piece(piece, pieces):
    color = piece.colour
    letter = piece.letter
    col_num, row_num = piece.grid_coord.col, piece.grid_coord.row
    print "possible_moves_for_piece: " + str((col_num, row_num))

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


def is_valid_movement_pattern_for_piece(piece, to_coord, pieces):
    to_grid_coord = chess_coord_to_grid_coord(to_coord)
    possible_moves = possible_moves_for_piece(piece, pieces)
    move_is_possible = to_grid_coord in possible_moves

    return move_is_possible, possible_moves



