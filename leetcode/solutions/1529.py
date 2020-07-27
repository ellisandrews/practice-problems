def num_flips(target):

    # Track number of flip operations
    flip_counter = 0

    # For each character in target (left to right) check if we need to do a flip from that bulb to the end of the array.
    # Once bulbs are visited in this algorithm, they are fixed and should match the target!
    for i in range(len(target)):
        
        # Check if number of flips is even currenly
        even_flips = flip_counter % 2 == 0

        # Conditions on which we flip
        if (target[i] == '1' and even_flips) or (target[i] == '0' and not even_flips):

            # Increment number of flips            
            flip_counter += 1
           
    # Return the number of flips (the solution)
    return flip_counter


# Test cases
assert num_flips('10111') == 3
assert num_flips('101') == 3
assert num_flips('00000') == 0
assert num_flips('001011101') == 5
