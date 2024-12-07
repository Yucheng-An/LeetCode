def kthSmallest(arr,k):
    if not arr:
        return -1
    maxElement = max(arr)
    count = [0] * (maxElement+1)
    for i in arr:
        count[i] += 1
    count1 = 0
    for i in range(len(count)):
        count1 += count[i]
        if count1 >= k:
            return i
    return -1
testcase = [7,10,4,3,20,15]
print(kthSmallest(testcase,2))
print(testcase)