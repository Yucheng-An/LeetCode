def getMinDiff(arr,k):
    arr.sort()
    for i in range(len(arr)):
        if i < len(arr)/2:
            arr[i] = arr[i] + k
        else:
            arr[i] = arr[i] - k
    print(f"Min:{min(arr)}")
    print(f"Max:{max(arr)}")
    return max(arr) - min(arr)


k = 3
arr = [3, 9, 12, 16, 20]
print(getMinDiff(arr,k))
