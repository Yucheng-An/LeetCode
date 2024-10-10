def example(num: int):
    sizeMatrix = num * 2 - 1
    matrix = [[num] * sizeMatrix] * sizeMatrix
    print(matrix)
    # return re(matrix, num, 0, sizeMatrix, 1)


def re(matrix, num, decreaseIndex ):
    if num - decreaseIndex == 1:
        matrix[(2*num-1)/2][(2*num-1)/2] = 1
        return matrix

    for i in range(0 + decreaseIndex, len(matrix) - )


res = example(3)
print(res)
