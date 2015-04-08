import directions as dire
from board_parts import GridCoord
import movement as mov


def check_if_piece_on_squares_in_between(squares_in_between, pieces):
    def piece_is_on_one_of_squares(piece, squares):
        hit_square = filter(lambda square: square.col is piece.grid_coord.col and
                         square.row is piece.grid_coord.row, squares)
        print "hit_square " + str(hit_square)
        return hit_square

    piece = filter(lambda piece: piece_is_on_one_of_squares(piece, squares_in_between), pieces)
    print "piece: " + str(piece) + " piece is not []: " + str((piece is []))
    return piece is []


def pawn_can_take_on_coords(piece_to_move, move_direction, col_new, row_new, pieces):
    take_directions = []

    if move_direction is dire.go_north:
        take_directions.append(dire.go_north_east)
        take_directions.append(dire.go_north_west)
    else:
        take_directions.append(dire.go_north_east)
        take_directions.append(dire.go_north_west)

    take_coordinates = map(lambda move_dir: move_dir(piece_to_move.grid_coord.col,
                                                     piece_to_move.grid_coord.row), take_directions)
    def piece_is_coord(coordss, piece):
        is_on = map(lambda coords: piece.grid_coord.col is coords[0] and piece.grid_coord.row is coords[1], coordss)
        return True in is_on

    move_is_take_coordinates = filter(lambda coords: coords[0] is col_new and coords[1] is row_new, take_coordinates)

    pieces_on_those_coordinates = filter(lambda piece: piece_is_coord(move_is_take_coordinates, piece), pieces)
    print "pieces_on_those_coordinates : " + str(pieces_on_those_coordinates)
    return pieces_on_those_coordinates is not []


def check_if_move_is_blocked(piece_to_move, col_new, row_new, possible_moves, pieces):
    is_blocked = False
    piece_to_take = None
    msg = ""

    print "col_new, row_new: " + str((col_new, row_new))
    col_new_grid, row_new_grid = mov.convert_from_chess_coor_to_grid(col_new, row_new)

    if piece_to_move.letter is 'Kn':
        is_blocked, piece_to_take, msg = examine_end_square(col_new, row_new, piece_to_move, pieces)
    elif piece_to_move.letter is 'P':
        move_direction, squares_in_between = dire.get_move_direction_and_squares_in_between(piece_to_move.grid_coord,
                                                                                            GridCoord(col_new_grid,
                                                                                                      row_new_grid),
                                                                                            dire.move_directions_queen())

        is_blocked, piece_to_take, msg = examine_end_square(col_new, row_new, piece_to_move, pieces)
        can_take = pawn_can_take_on_coords(piece_to_move, move_direction, col_new, row_new, pieces)

        print "can_take: " + str(can_take)

        print "squares_in_between : " + str(squares_in_between)
        piece_in_between = check_if_piece_on_squares_in_between(squares_in_between, pieces)
        print "piece_in_between : " + str(piece_in_between)



    return is_blocked, piece_to_take, msg, possible_moves


def examine_end_square(col_new, row_new, piece_to_move, pieces):
    is_blocked = False
    piece_to_take = None
    msg = ""

    piece_on_end_square = filter(lambda other_piece: other_piece.chess_coord.col is col_new and
                                        other_piece.chess_coord.row is row_new, pieces)

    print "pieces on end square: " + str(piece_on_end_square)

    if piece_on_end_square:
        piece_on_end_square = piece_on_end_square[0]

        if piece_on_end_square.colour is piece_to_move.colour:
            is_blocked = True
            msg = "Own piece on that square"
        else:
            piece_to_take = piece_on_end_square

    return is_blocked, piece_to_take, msg