


def helper(m):
    res = []
    row = 0
    colum = 0
    mcolumn = len(m)
    mrow = len(m[0])
    for i in range(0,len(m[0])):
        res.append(m[0][i])
    for i in range(1,len(m)):
        res.append(m[i][-1])
    for i in range(len(m[0])-1,1,-1):
        res.append(m[-1][i])
    for i in range(len(m)-1,1,-1):
        res.append(m[i][0])
    return res 

m = [[1,2,3],[4,5,6],[7,8,9]]
print(helper(m))