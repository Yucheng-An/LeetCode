def findDuplicates(arr):
    setlist = set()
    for i in arr:
        setlist.add(i)
        
    resultset = set()
    for i in arr:
        if i in setlist:
            arr.remove(i)
    return list(resultset)
    




test=[2,1, 3, 1, 2, 3]
print(findDuplicates(test))