def getMinDiff(arr,k):
    arr.sort()
    for i in range(len(arr)):
        if i < len(arr)/2:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] - k
    return max(arr) - min(arr)



