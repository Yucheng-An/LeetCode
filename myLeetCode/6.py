def convert(s, numRows):
    if numRows == 1:
        return s
    res = []
    for i in range(3):
        res.append([])
    j = 0
    for i in range(len(s)):
        res[j].append(s[i])
        j += 1
        if j == numRows:
            j = 0
    finalres = ""
    for i in res:
        
    