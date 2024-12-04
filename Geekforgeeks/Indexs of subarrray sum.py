def subArraySum(arr, target):
    fsum, left, res = 0, 0, []
    while left < len(arr):
        res.append(left + 1)
        for i in range(left, len(arr)):
            fsum = fsum + arr[i]
            if fsum > target:
                left += 1
                fsum = 0
                res.clear()
            if fsum == target:
                res.append(i + 1)
                return res
    return [-1]


testcase = [1, 2, 3, 7, 5]
target = 12
print(subArraySum(testcase, target))
