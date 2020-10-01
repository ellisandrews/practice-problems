from typing import List


# Brute force
def max_coins_bf(piles: List[int]) -> int:

    # The triplet you want to pick is:
    # (lowest, second highest, highest)

    # First, sort the list, as order doesn't matter

    # Pop one off the front, two off the back every time, and that's your triplet
    # Alternatively, pop one off front and back right away, then pop one off back and that's *your* pile

    # Sum your pile

    sorted_piles = sorted(piles)

    your_total = 0

    while sorted_piles:
        sorted_piles.pop(0)
        sorted_piles.pop(-1)
        your_total += sorted_piles.pop(-1)

    return your_total



# More efficient

def max_coins(piles: List[int]) -> int:

    # Sort the list
    sorted_piles = sorted(piles)

    # Disregard the first 1/3 of the list
    num_piles = len(sorted_piles)

    # Sum every other element of second 2/3 of sorted list
    return sum(sorted_piles[i] for i in range(int(num_piles/3), num_piles, 2))




# Test cases

assert max_coins([2,4,1,2,7,8]) == 9
assert max_coins([2,4,5]) == 4
assert max_coins([9,8,7,6,5,1,2,3,4]) == 18
