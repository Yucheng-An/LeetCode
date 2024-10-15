def search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + ((right - left)//2)
        if nums[mid] = 

nums = [-1,0,2,3,5,9,12]
target = 2

print(search(nums,target))