def minJumps(self, arr):
    if len(arr) == 1:
        return 0

    jump = 0
    end = 0
    farest = 0
    for i in range(len(arr)-1):
        farest = max(farest, i+arr[i])
        if i == end:
            jump += 1
            end = farest
        if end < i + 1:
            return -1
    return jump