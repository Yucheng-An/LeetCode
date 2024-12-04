def maxSubArraySum(arr):
    left = 0
    maxResult = float("-inf")
    currentSum = 0
    for i in range(len(arr)):
        currentSum += arr[i]
        if currentSum > maxResult:
            maxResult = currentSum
        subCurrentSum = currentSum
        while left <= i:
            subCurrentSum -= arr[left]
            if subCurrentSum > maxResult:
                maxResult = subCurrentSum
            left += 1
        left = 0
    return maxResult

test = [-2,-4]
print(maxSubArraySum(test))
