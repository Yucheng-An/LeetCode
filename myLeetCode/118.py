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
    if numRows == 1:
        return dp
    for i in range(len(dp)):
        for j in range(1,len(dp[i])):
            dp[]
    return dp


t = generate(1)
print(t)
