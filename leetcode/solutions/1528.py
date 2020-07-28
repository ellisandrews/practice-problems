def shuffle_string(s, indices):
    # Length of the input string (and index array)
    s_length = len(s)

    # List to hold the final order of letters for the output string
    final_string_list = [None for _ in range(s_length)]

    # Populate the list with the correct order of letters
    for i in range(s_length):
        final_string_list[indices[i]] = s[i]

    # Join the list of letters into the final string and return it
    return ''.join(final_string_list)


# Test cases
assert shuffle_string('codeleet', [4,5,6,7,0,2,1,3]) == 'leetcode'
assert shuffle_string('abc', [0,1,2]) == 'abc'
assert shuffle_string('aiohn', [3,1,4,2,0]) == 'nihao'
assert shuffle_string('aaiougrt', [4,0,2,6,7,3,1,5]) == 'arigatou'
assert shuffle_string('art', [1,0,2]) == 'rat'
