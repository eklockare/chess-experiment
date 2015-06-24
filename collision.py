import directions as dire
from board_parts import GridCoord, ChessCoord
import movement as mov
import board_parts as bps


def check_if_piece_on_squares_in_between(squares_in_between, pieces):
    def piece_is_on_one_of_squares(piece, squares):
        hit_square = filter(lambda square: square.col is piece.grid_coord.col and
                         square.row is piece.grid_coord.row, squares)
        return hit_square

    piece = filter(lambda piece: piece_is_on_one_of_squares(piece, squares_in_between), pieces)
    print "piece: " + str(piece) + " piece is not []: " + str((piece is []))
    return piece is []


def check_if_move_is_blocked(piece_to_move, new_coordinates, possible_moves, pieces):
    is_blocked = False
    is_valid_movement = False
    piece_to_take = None
    msg = ""

    print "new_coordinates: " + str(new_coordinates)
    grid_coord = bps.chess_coord_to_grid_coord(new_coordinates)

    if piece_to_move.letter is 'Kn':
        is_blocked, piece_to_take, msg = examine_end_square(new_coordinates, piece_to_move, pieces)
    elif piece_to_move.letter is 'P':
        print "piece_to_move.grid_coord.col %s  piece_to_move.grid_coord.row %s " % \
              (piece_to_move.grid_coord.col, piece_to_move.grid_coord.row)

        is_valid_movement, move_direction, squares_in_between = \
            dire.get_move_direction_and_squares_in_between(piece_to_move.grid_coord,
                                                           grid_coord,
                                                           dire.move_directions_queen())

        is_taking_move = dire.is_diagonal_move(move_direction)
        is_blocked, piece_to_take, msg = examine_end_square(new_coordinates, piece_to_move, pieces)

        can_take = piece_to_take and is_taking_move
        print "can_take %s " % can_take

        print "squares_in_between : " + str(squares_in_between)
        piece_in_between = check_if_piece_on_squares_in_between(squares_in_between, pieces)
        print "piece_in_between : " + str(piece_in_between)

        is_valid_movement = can_take or is_valid_movement

    print "is_valid_movement %s, is_blocked, %s piece_to_take %s, msg %s, possible_moves: %s" % \
          (is_valid_movement, is_blocked, piece_to_take, msg, possible_moves)
    return is_valid_movement, is_blocked, piece_to_take, msg, possible_moves


def examine_end_square(new_coordinates, piece_to_move, pieces):
    is_blocked = False
    piece_to_take = None
    msg = ""

    piece_on_end_square = filter(lambda other_piece: other_piece.chess_coord == new_coordinates,
                                 pieces)

    print "pieces on end square: " + str(piece_on_end_square)

    if piece_on_end_square:
        piece_on_end_square = piece_on_end_square[0]

        if piece_on_end_square.colour is piece_to_move.colour:
            is_blocked = True
            msg = "Own piece on that square"
        else:
            piece_to_take = piece_on_end_square

    return is_blocked, piece_to_take, msg