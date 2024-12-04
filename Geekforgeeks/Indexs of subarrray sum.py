def subArraySum(arr, target):
    sum,left,res = 0,0,[]
    while left < len(arr):
        res.append(left+1)
        for i in range(left,len(arr)):
            sum = sum + arr[i]
            if sum > target:
                left += 1
                sum = 0
                res.clear()
            if sum == target:
                res.append(i+1)
                return res
    return [-1]
testcase = [1,2,3,7,5]
target = 12

target = 12 
# print(subArraySum(testcase,target))