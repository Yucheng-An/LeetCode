def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pairs = helper(nums, i + 1, -nums[i])
        for pair in pairs:
            res.append([nums[i]] + pair)
    return res


def helper(nums, start, target):
    pairs = []
    left = start
    right = len(nums) - 1
    while left < right:
        if target == nums[left] + nums[right]:
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif target > nums[left] + nums[right]:
            left += 1
        else:
            right -= 1
    return pairs
