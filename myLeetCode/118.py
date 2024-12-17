def generate(numRows):
    res = []
    for i in range(numRows):
        subArray = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                subArray.append(1)
            else:
                subArray.append(0)
        res.append(subArray)
    return res


t = generate(5)
print(t)
