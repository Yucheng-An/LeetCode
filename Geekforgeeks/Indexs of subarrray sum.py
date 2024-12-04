def subArraySum(arr, target):
    sum = 0
    res = []
    left = 0
    while left < len(arr):
        for i in range(left,len(arr)):
            sum += arr[i]
            res.append(i)
            if sum > target:
                left += 1
                sum = 0
                res = []
                break
            if sum == target:
                return res
    return [-1]

testcase = [1,2,3]

target = 12 
print(subArraySum(testcase,target))