def arrayRankTransform(arr):
    for index, value in enumerate(arr):
        arr[index] = (value, index, 0)
    arr.sort(key=lambda x: x[0])
    rank = 1
    arr[0] = (arr[0][0], arr[0][1], rank)
    print(arr)
    for i in range(1, len(arr)):
        if arr[i][0] == arr[i - 1][0]:
            arr[i] = (arr[i][0], arr[i][1], rank)
        else:
            rank += 1
            arr[i] = (arr[i][0], arr[i][1], rank)
    arr.sort(key=lambda x: x[1])
    res = []
    for i in range(len(arr)):
        res.append(arr[i][2])
    return res


arr = [40, 10, 20, 30]
print(arrayRankTransform(arr))
