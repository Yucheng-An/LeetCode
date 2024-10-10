def example(num: int):
    sizeMatrix = num * 2-1
    matrix = [[0]*sizeMatrix] * sizeMatrix
    startNumber = len(matrix)
    for i in range(startNumber):
        for j in range(startNumber):
            matrix[i][j] = startNumber - i -
    print(matrix)




example(3)