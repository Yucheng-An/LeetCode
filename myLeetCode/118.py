def generate(numRows):
    res = []
    for i in range(numRows):
        t = []
        for j in range(0,i):
            res.append(1)
    return res



t = generate(5)
print(t)