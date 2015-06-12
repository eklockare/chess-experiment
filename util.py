


def compare_lists(one, two):
    if len(one) != len(two):
        return False

    def comparisons(check, list):
        return map(lambda el: el == check, list)

    compares = map(lambda t: comparisons(t, one), two)
    flatten_compares = flatten_list(compares)
    count_true = flatten_compares.count(True)

    return count_true == len(one)



def flatten_list(list):
    return [item for sublist in list for item in sublist]
