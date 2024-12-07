def kthSmallest(arr,k):
    maxElement = max(arr)
    count = [0] * (maxElement+1)
    for i in arr:
        count[i] += 1
    

testcase = [7,10,4,3,20,15]
print(kthSmallest(testcase,2))
print(testcase)