def generate(numRows):
    res = []
    for i in range(numRows):
        subArray = []
        for j in range(0,i+1):
            subArray.append(1)
        res.append(subArray)
    return res



t = generate(5)
print(t)