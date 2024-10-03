class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[0][0]
        result = ["null"]
        for i in range(1,len(nums)):
            obj = self.sumRange(self.nums,nums[i][:][0],nums[i][:][1])
            result.appen(obj)
        return result


    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left,right+1):
            sum += self.nums[i]
        return sum