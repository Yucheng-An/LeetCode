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
    count = 0 
    for i in arr:
        if i == candidate:
            count += 1
    if count > len(arr):
        return candidate
    else:
        return -1


print(majorityElement([3,1,3,3,2]))
