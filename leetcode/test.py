def arrayRankTransform(arr):
    for index, value in enumerate(arr):
        arr[index] = (value, index, 0)
    arr.sort(key=lambda x: x[0])
    rank = 1
    arr[1] = (arr[0][0],arr[0][1],rank)
    for i in range(1,len(arr)):
        if arr[i][0] == arr[i-1][0]
            arr[i]= (arr[i][0],arr[i][1],rank)

arr = [40, 10, 20, 30]
arrayRankTransform(arr)
