


def helper(m):
    res = []
    row = 0
    colum = 0
    mcolumn = len(m)
    mrow = len(m[0])
    for i in range(len(m[0])):
        res.append(m[0][i])
    for i in range(1,len(m)):
        res.append(m[i][-1])
    for i in range(len(m[0])):