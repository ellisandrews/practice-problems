def max_unique_split(s: str) -> int:
    
    # Container to track already used substrings
    used_substrings = set()
    
    current_substring = ''
    
    for i, char in enumerate(s):
        
        # Add the character to the current substring
        current_substring += char
        
        # If it's a new unique substring, append to the set and reinitialize the current substring
        if current_substring not in used_substrings:
            used_substrings.add(current_substring)
            current_substring = ''
    
    # Return the number of substrings
    return len(used_substrings)



# --- Test Cases --- #

assert max_unique_split("ababccc") == 5
assert max_unique_split("aba") == 2
assert max_unique_split("aa") == 1
