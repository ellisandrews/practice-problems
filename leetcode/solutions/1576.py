def modify_string(s: str) -> str:

    letters = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    }

    new_s = ''

    for i, char in enumerate(s):

        # Can't modify existing letters
        if char != '?':
            new_s += char
            continue

        # Handle '?'

        # Get previous and following characters, which cannot be used
        previous_char = new_s[i-1] if new_s else '?'
        next_char = s[i+1] if i < len(s) - 1 else '?'

        # Get possible replacement letters for the '?'
        possible_replacements = list(letters.difference({previous_char, next_char}))

        # Just grab the first one
        new_s += possible_replacements[0]

    return new_s
