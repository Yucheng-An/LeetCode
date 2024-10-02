def arrayRankTransform(arr):
    for index, value in enumerate(arr):
        arr[index] = (value, index, 0)
    arr.sort(key=lambda x: x[0])
    for i in range(len(arr)):
        arr[i]= (arr[i])

arr = [40, 10, 20, 30]
arrayRankTransform(arr)
