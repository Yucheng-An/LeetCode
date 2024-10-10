def example(num: int):
    sizeMatrix = num * 2-1
    matrix = [[3]*sizeMatrix] * sizeMatrix
    print(matrix)
    startNumber = num
    print(startNumber)
    for i in range(0,len(matrix)):
        for j in range(0 , len(matrix)):
            matrix[i][j] = startNumber
    print(matrix)




example(3)