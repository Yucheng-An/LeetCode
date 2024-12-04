def findDuplicates(arr):
    resSet = set()
    res = set()
    for i in arr:
        if i in resSet:
            res.add(i)
        else:
            resSet.add(i)
    return list(res)
            
            




test=[2,1, 3, 1, 2, 3]
print(findDuplicates(test))