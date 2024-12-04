def subArraySum(self, arr, target):
    sum = 0
    res = []
    left = 0
    while left < len(arr):
        res.append(left+1)
        for i in range(left,len(arr)):
            sum = sum + arr[i]
            if sum > target:
                sum = 0
                res.clear()
                break
            if sum == target:
                res.append(i+1)
                return res
        res.clear()
        left += 1
    return [-1]


testcase = [1, 2, 3, 7, 5]
target = 12
print(subArraySum(testcase, target))
