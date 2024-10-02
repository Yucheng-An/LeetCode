def arrayRankTransform(arr):
    for index, value in enumerate(arr):
        arr[index] = (value, index, 0)
    arr.sort(key=lambda x: x[0])
    rank = 1
    for i in range(1,len(arr)):
        if arr[i]
            arr[i]= (arr[i][0],arr[i][1],rank)

arr = [40, 10, 20, 30]
arrayRankTransform(arr)
