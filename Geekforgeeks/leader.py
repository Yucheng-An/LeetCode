def leaders(arr):
    res = []
    for i in (0,len(arr)-1):
        if arr[i]<arr[i+1]:
            initLeader = arr[i+1]
            res.append(initLeader)
    return res

arr = [16, 17, 4, 3, 5, 2]
lea