

def spiralOrder(m):
    mcolumn = len(m)
    mrow = len(m[0])
    while 


def helper(m, mcolumn, mrow):
    res = []
    for i in range(0,mrow):
        res.append(m[0][i])
    for i in range(1,mcolumn):
        res.append(m[i][-1])
    for i in range(mrow-2,-1,-1):
        res.append(m[-1][i])
    for i in range(mrow-2,0,-1):
        res.append(m[i][0])
    return res 

m = [[1,2,3],[4,5,6],[7,8,9]]
print(helper(m))


def helper1 (m,rowstart,rowend, columnstart, columnend):
    res = []
    for i in range(rowend-rowstart+1):
        res.append(row)