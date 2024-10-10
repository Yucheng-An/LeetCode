def example(num: int):
    sizeMatrix = num * 2-1
    matrix = [[0]*sizeMatrix] * sizeMatrix
    startNumber = num
    print(startNumber)
    for i in range(0,startNumber):
        for j in range(i,startNumber):
            matrix[i][j] = startNumber - i
    print(matrix)




example(3)