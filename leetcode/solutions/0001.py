from typing import List


def two_sums(numbers: List[int], target: int) -> List[int]:
    # Brute force solution -- double for-loop O(n^2)
    for index_1, num_1 in enumerate(numbers):
        for index_2, num_2 in enumerate(numbers):
            if index_1 != index_2 and num_1 + num_2 == target:
                return [index_1, index_2]


# Test cases
assert two_sums([2, 7, 11, 15], 9) == [0, 1]
