


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
