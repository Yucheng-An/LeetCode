def example(num: int):
    sizeMatrix = num * 2 - 1
    matrix = [[0] * sizeMatrix] * sizeMatrix
    res1 = re(matrix, num, 0)
    return res1


def re(matrix, num, decreaseIndex):
    if num - decreaseIndex == 0:
        matrix[(2 * num - 1) // 2][(2 * num - 1) // 2] = 1
        return matrix

    else:
        for i in range(0 + decreaseIndex, len(matrix) - decreaseIndex):
            for j in range(0 + decreaseIndex, len(matrix) - decreaseIndex):
                matrix[i][j] = num - decreaseIndex

        return re(matrix, num, decreaseIndex + 1)


res = example(3)
print(res)
