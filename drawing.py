import board_parts as bps

def get_row_colour(row_id):
    coloured = []
    for row in bps.NUM_ROWS:
        if (row + row_id) % 2 == 0:
            coloured.append(bps.white)
        else:
            coloured.append(bps.black)
    return coloured

def row_id_to_row_no(row_id):
    return str(8 - row_id)

def add_row_number(row_part, square_colour, row, col):
    if col is 7:
        last_bit = square_colour(row_part + '  ' + row_id_to_row_no(row))
    else:
        last_bit = square_colour(row_part)

    return last_bit

def apply_colouring_to_row_part(row_id, colouring, pieces, row_part_is_piece, last_move):
    row_part, is_piece_part_row = row_part_is_piece
    colouring_row_parts = zip(colouring, row_part)

    def paint_last_square_of_row(square_colour, (_, row_part), row, col):
        number_added = add_row_number(row_part, square_colour, row, col)
        return number_added


    def paint_row(square_coloring, (_, row_part)):
        return square_coloring(row_part)

    def paint_row_with_piece(square_colour, piece_colour, letter, row, col):
        last_bit = add_row_number('  |', square_colour, row, col)

        return square_colour('|  ') + piece_colour(letter) + last_bit


    def get_square_color(row_id, col, last_move):
        square_colour, _ = colouring_row_parts[col]
        if last_move:
            from_row, from_col, to_row, to_col = last_move
            if col == from_col and row_id == from_row:
                return bps.yellow_background
            elif col == to_col and row_id == to_row:
                return bps.green_background
            else:
                return square_colour
        else:
            return square_colour

    result = []
    for col in range(0, len(colouring_row_parts)):
        piece_on_this_col = filter(lambda piece: piece.grid_coor.col is col, pieces)
        square_colour = get_square_color(row_id, col, last_move)

        if is_piece_part_row and piece_on_this_col:
            piece = piece_on_this_col[0]
            row, col = piece.grid_coor.row, piece.grid_coor.col
            result.append(paint_row_with_piece(square_colour, piece.colour, piece.symbol, row, col))
        elif is_piece_part_row:
            result.append(paint_last_square_of_row(square_colour, colouring_row_parts[col], row_id, col))
        else:
            result.append(paint_row(square_colour, colouring_row_parts[col]))

    return result


def apply_colouring_to_row(row_id, (colour, (pieces, row)), last_move):
    color_row_parts = map(lambda row_part: apply_colouring_to_row_part(row_id, colour, pieces, row_part, last_move), row)
    return color_row_parts


def piece_is_on_row(piece, row):
    # prow, _, _, _ = piece
    prow = piece.grid_coor.row
    return prow is row


def get_row_with_pieces(pieces, row_num):
    row_pieces = filter(lambda piece: piece_is_on_row(piece, row_num), pieces)

    if row_num is 0:
        return row_pieces, bps.top_row()
    else:
        return row_pieces, bps.middle_row()


def all_rows(pieces):
    rows = []

    for row in bps.NUM_ROWS:
        rows.append((row, get_row_with_pieces(pieces, row)))

    return rows



def draw_board(pieces, last_move):
    all_colouring = map(get_row_colour, bps.NUM_ROWS)
    all_rows_with_colour_and_pieces = zip(all_colouring, all_rows(pieces))

    def apply_colouring_to_row_last_move((colour, (row_id, (pieces, row)))):
        return apply_colouring_to_row(row_id, (colour, (pieces, row)), last_move)


    all_rows_coloured = map(apply_colouring_to_row_last_move, all_rows_with_colour_and_pieces)


    for row in all_rows_coloured:
        for elem in row:
            print("{: >16} {: >16} {: >16} {: >16} {: >16} {: >16} {: >16} {: >16}".format(*elem))
