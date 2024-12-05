def minJump(nums):
    jumps = 0
    = = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_jump_end:
            jumps += 1
            current_jump_end = farthest
    return jumps



test=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJump(test))