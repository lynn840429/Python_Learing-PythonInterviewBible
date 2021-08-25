def show_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    row, col = 0, 0
    num, direction = 1, 0

    while num <= n ** 2:
        if matrix[row][col] == 0:
            matrix[row][col] = num
            num += 1
        if direction == 0:
            if col < n - 1 and matrix[row][col + 1] == 0:
                col += 1
            else:
                direction += 1
        elif direction == 1:
            if row < n - 1 and matrix[row + 1][col] == 0:
                row += 1
            else:
                direction += 1
        elif direction == 2:
            if col > 0 and matrix[row][col - 1] == 0:
                col -= 1
            else:
                direction += 1
        else:
            if row > 0 and matrix[row - 1][col] == 0:
                row -= 1
            else:
                direction += 1
        direction %= 4
    for x in matrix:
        for y in x:
            print(y, end='\t')
        print()


show_spiral_matrix(4)

#-------------------------------------------------#
def show_spiral_matrix_ver2(n):
    matrix = [i+1 for i in range(n**2)]
    result = [[0]*n for _ in range(n)]

    layer = n - 2

    for i in range(n):
        pass
        # Dir 1 #
        result[0][0:n-1] = [i+1 for i in range(n-1)]
        # Dir 2 #
        print(result[1][2])
        # Dir 3 #

        # Dir 4 #

        layer -= 1

    print(result)

show_spiral_matrix_ver2(3)