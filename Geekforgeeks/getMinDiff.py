def getMinDiff(arr,k):
    arr.sort()
    for i in range(len(arr)):
        if i < len(arr)/2:
            