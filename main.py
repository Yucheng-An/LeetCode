def example(num: int):
    sizeMatrix = num * 2-1
    matrix = [[3]*sizeMatrix] * sizeMatrix
    print(matrix)
    print(num)
    for i in range(0,len(matrix)):
        for j in range(0 , len(matrix)):
            matrix[i][j] = num
    print(matrix)




example(3)