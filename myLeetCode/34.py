def searchRange(nums, target):
    return [left_bound(nums,target),right_bound(nums,target)]

def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            right = mid - 1
    if left < 0 or left >= len(nums):
        return -1
    return left if nums[left] == target else -1
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            left = mid + 1
    if right < 0 or right >= len(nums):
        return -1
    return right if nums[right] == target else -1


nums = [5,5,7,7,7,8,8,8,8,8,]