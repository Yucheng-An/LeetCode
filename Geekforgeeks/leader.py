def leaders(self, arr):
    initLeader = 0
    res = []
    for i in (0,len(arr)-1):
        if arr[i]>arr[i+1]:
            initLeader = arr[i]
            res.append(arr[i])
    return res