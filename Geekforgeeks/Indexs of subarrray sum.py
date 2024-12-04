def subArraySum(arr, target):
    sum = 0
    res = []
    left = 0
    while left < len(arr):
        res.append(left+1)
        for i in range(left,len(arr)):
            sum = sum + arr[i]
            if sum > target:
                res.clear()
                break
            if sum == target:
                res.append(i+1)
                return res
        sum =0
        res.clear()
        left += 1
    return [-1]

# O(n^2)

def subArraySum2(arr, target):
   start = 0
   currSum = 0
   for i in arr:
       currSum 
testcase = [22,9,47,33,32]
target = 145
print(subArraySum(testcase, target))
