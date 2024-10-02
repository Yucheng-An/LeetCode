def arrayRankTransform(self, arr):
    for index, value in enumerate(arr):
        arr[index] = (value,index,0)
    arr.sort(key=lambda x : x[0])
    pointer = 0
    rank = 1
    arr[0][3] = 1
    
