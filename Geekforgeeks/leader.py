def leaders(arr):
    initLeader = 0
    res = []
    for i in (0,len(arr)-1):
        if arr[i]>arr[i+1]:
            initLeader = arr[i]
            res.append(initLeader)
    return res

