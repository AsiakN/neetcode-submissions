class Solution:
    def findMin(self, nums: List[int]) -> int: 
        min_num = math.inf
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
        return int(min_num)
