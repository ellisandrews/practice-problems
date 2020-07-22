"""
Write a program which takes as input a sorted array and updates it so that all duplicates have been removed.
Return the valid number of elements.

Input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
Intermediate: [2, 3, 5, 7, 11, 13]
Output: 6

Hint: There is an O(n) time and O(1) space solution
"""

def remove_duplicates(array):

    # BRUTE FORCE
    # COMPLEXITY:
    #   Space: O(n)
    #   Time: O(n)

    # Make a new array
    no_dups_array = []

    # Iterate over the input array, if the element is different from the last one, append it to the new array
    for index, item in enumerate(array):
        if index == 0:
            no_dups_array.append(item)
        else:
            if item != array[index - 1]:
                no_dups_array.append(item)

    # Return the length of the new array
    return len(no_dups_array)

# Test
input_list = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(remove_duplicates(input_list))  # Should be 6
