def count_odds(low: int, high: int):

    low_odd = low % 2 != 0
    high_odd = high % 2 != 0
    diff = high - low

    if low_odd and high_odd:
        return int(diff / 2) + 1
    elif (not low_odd) and (not high_odd):
        return int(diff / 2)
    else:
        return int(diff / 2 + 0.5)


# Test cases
assert count_odds(3, 7) == 3
assert count_odds(8, 10) == 1
assert count_odds(3, 10) == 4
assert count_odds(4, 15) == 6
