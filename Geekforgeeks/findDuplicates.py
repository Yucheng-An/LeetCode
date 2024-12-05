def minJump(nums):
    jumps = 0
    current_jump_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest
    return jumps



test=[2, 3, 1, 2, 3]
print()