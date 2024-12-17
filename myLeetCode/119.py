def getRow(self, rowIndex: int):
    numRows = rowIndex + 1
    dp = []
    for i in range(numRows):
        subArray = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                subArray.append(1)
            else:
                subArray.append(0)
        dp.append(subArray)
    if numRows == 1 or numRows == 2:
        return dp[rowIndex]
    for i in range(2, len(dp)):
        for j in range(1,len(dp[i])-1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[rowIndex]