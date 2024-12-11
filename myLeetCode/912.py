# Using divide-conquer to sort array
def myArray(self, nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    right = myArray(nums[:mid])
    left = myArray(nums[mid:])
    return meger(right, left)


def sortArray(nums):
    return myArray(nums)


def meger(right, left):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
