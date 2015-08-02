def compare_lists(one, two):
    if len(one) != len(two):
        return False

    def comparisons(check, other):
        return map(lambda el: el == check, other)

    def counts(check, the_list):
        return check, the_list.count(check)

    counts_in_list_one = map(lambda o: counts(o, one), one)
    counts_in_list_two = map(lambda t: counts(t, two), two)

    compares = map(lambda t: comparisons(t, counts_in_list_one), counts_in_list_two)
    flatten_compares = flatten_list(compares)
    count_true = flatten_compares.count(True)
    return count_true == len(one)


def flatten_list(to_flatten):
    return [item for sub_list in to_flatten for item in sub_list]

def select_piece(selected_coordinates, pieces):
    piece_selection = filter(lambda piece: piece.chess_coord ==
                                           selected_coordinates, pieces)
    if len(piece_selection) > 0:
        return piece_selection[0]
    else:
        return None

def select_pieces(multiple_coordinates, pieces):
    return map(lambda coord: select_piece(coord, pieces), multiple_coordinates)
