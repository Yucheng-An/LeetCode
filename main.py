def example(num: int):
    sizeMatrix = num * 2-1
    matrix = [[0]*sizeMatrix] * sizeMatrix
    startNumber = num
    print(startNumber)
    for i in range(0,len(matrix)):
        for j in range(0 , len(0)):
            matrix[i][j] = startNumber
    print(matrix)




example(3)