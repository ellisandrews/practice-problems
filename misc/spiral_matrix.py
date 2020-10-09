def round_trip(matrix, x_start, y_start, x_end, y_end):

    # Top row (left to right)
    for val in matrix[y_start][x_start:x_end]:
        print(val)

    # Right side
    for array in matrix[y_start+1:y_end]:
        print(array[x_end-1])

    # Bottom row (right to left)
    for val in reversed(matrix[y_end-1][x_start:x_end-1]):
        print(val)

    # Left side
    for array in reversed(matrix[y_start+1:y_end-1]):
        print(array[x_start])


def print_spiral_matrix(matrix):

    # Matrix is a 2D array of integers

    x_start = 0
    y_start = 0
    x_end = len(matrix[0])
    y_end = len(matrix)

    while True:

        round_trip(matrix, x_start, y_start, x_end, y_end)

        x_start += 1
        y_start += 1

        x_end -= 1
        y_end -= 1
    
        if x_start == 2:
            break


mat = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19]
]

print_spiral_matrix(mat)
