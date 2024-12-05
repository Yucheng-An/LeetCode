def leaders(arr):
    res = []
    currentMax = float("-inf")
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] >= currentMax:
            res.append(arr[i])
            currentMax = arr[i]
    res.reverse()
    return res


arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", leaders(arr))
