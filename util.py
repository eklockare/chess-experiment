def compare_lists(one, two):
    if len(one) != len(two):
        return False

    def comparisons(check, other):
        return map(lambda el: el == check, other)

    compares = map(lambda t: comparisons(t, one), two)
    flatten_compares = flatten_list(compares)
    count_true = flatten_compares.count(True)

    return count_true == len(one)


def flatten_list(to_flatten):
    return [item for sub_list in to_flatten for item in sub_list]

def select_piece(selected_coordinates, pieces):
    piece_selection = filter(lambda piece: piece.chess_coord ==
                                           selected_coordinates, pieces)
    return piece_selection[0]

def select_pieces(multiple_coordinates, pieces):
    return map(lambda coord: select_piece(coord, pieces), multiple_coordinates)
