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
    
    return dp


t = generate(1)
print(t)
