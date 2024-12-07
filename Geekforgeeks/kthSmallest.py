def kthSmallest(arr,k):
    # k = 1 to find the smallest element
    
    candidate = float("inf")
    for i in arr:
        if i < candidate:
            candidate = i
            arr.remove(i)
    return candidate

testcase = [7,10,4,3,20,15]
print(kthSmallest(testcase,0))
print(testcase)