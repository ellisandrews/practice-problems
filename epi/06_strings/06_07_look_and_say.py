"""
The look-and-say sequence -- read off the digits of the previous entry, counting the number of digits in goups of the same digit.

First 8 numbers in the sequence are (starting at 1): [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211]

Write a program that takes as input an integer `n` and returns the `nth` integer in the sequence. Return the result as a string.
"""


# Write a function to get the next number in the sequence, given the previous number
def get_next_number(previous: str) -> str:

    # Split previous number into groups of consecutive like digits
    # e.g. '111223' -> ['111', '22', '3']
    previous_length = len(previous)
    groups = []
    start_index = 0

    for i in range(previous_length):

        # Handle iteration at the end so we don't get an index error
        if i == previous_length - 1:
            groups.append(previous[start_index:])

        # If the next character is different, add slice of string representing group to the `groups` list
        elif previous[i] != previous[i+1]:
            groups.append(previous[start_index:i+1])
            start_index = i + 1

    # Create the new string by counting digits in each group
    # e.g. '111' -> '31', '22' -> '22', '3' -> '13'
    group_contributions = [f"{len(group)}{group[0]}" for group in groups]

    # Concatenate the groups at the end and return
    # e.g. '31' + '22' + '13' -> '312213'
    return ''.join(group_contributions)


def nth_look_and_say(n):    
    # Recursively find the nth number by calculating the next number given the previous
    if n == 1:
        return '1'
    
    return get_next_number(nth_look_and_say(n-1))


# Test cases
assert get_next_number('1') == '11'
assert get_next_number('11') == '21'
assert get_next_number('21') == '1211'
assert get_next_number('1211') == '111221'
assert get_next_number('111221') == '312211'
assert get_next_number('312211') == '13112221'

assert nth_look_and_say(1) == '1'
assert nth_look_and_say(2) == '11'
assert nth_look_and_say(3) == '21'
assert nth_look_and_say(4) == '1211'
assert nth_look_and_say(5) == '111221'
assert nth_look_and_say(6) == '312211'
assert nth_look_and_say(7) == '13112221'
