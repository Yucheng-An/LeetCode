def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height)-1
    maxArea = 0
    while left < right:
        thisArea = min(height[left],height[right]) * (right-left)
        maxArea = thisArea if maxArea < thisArea else maxArea
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea