def generate(numRows):
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
        return dp
    for i in range(2, len(dp)):
        for j in range(,len(dp[i])-1):
            dp[i][j] = 9
    return dp


t = generate(2)
print(t)
