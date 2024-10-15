def search(nums, target):
    return binarySearch(nums,target,0,len(nums)-1)

def binarySearch(nums,target,left,right):
    while left < right:
        mid = left + ((right - left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

