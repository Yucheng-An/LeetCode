def myArray(self, nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2
    right = self.myArray(nums[:mid])
    left = self.myArray(nums[mid:])
    return self.meger(right,left)

def sortArray(self, nums: List[int]):
    return self.myArray(nums)

def meger(self, right,left):
    result = []
    i = 0
    j = 0
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
        i+=1
    while j < len(right):
        result.append(right[j])
        j+=1
    return result