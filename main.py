def example(num: int):
    sizeMatrix = num * 2 - 1
    matrix = [[num] * sizeMatrix] * sizeMatrix
    print(matrix)
    return re(matrix, num, 0, sizeMatrix, )


def re(matrix, num, size, needCall):
    if needCall == 1:
        matrix[start][end] = 1



res = example(3)
print(res)
