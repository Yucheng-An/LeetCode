def majorityElement(arr):
    candidate = None
    count = 0
    for i in arr:
        if count == 0:
            candidate = i
            count += 1
        elif i == candidate:
            count += 1
        else:
            count -= 1
    
    a = 0
    for i in arr:
        if i == candidate:
            a += 1
    if a >= len(arr)/2:
        return candidate
    else:
        return -1


print(majorityElement([3, 2, 3, 3, 2]))
