def example(num: int):
    sizeMatrix = num * 2 - 1
    matrix = [[num] * sizeMatrix] * sizeMatrix
    for i in range(sizeMatrix):
        for j in range(sizeMatrix):


def re(matrix, num, start, end):
    if start == end:
        matrix[start][end] = 1;
        return matrix
    for i in range(start, end):
        for j in range(start, end):
            matrix[i][j] = num
    re()

example(3)
