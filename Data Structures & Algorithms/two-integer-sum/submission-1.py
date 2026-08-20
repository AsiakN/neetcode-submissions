class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        brute force: two loops for each, then return index
        optimal solution : create dictionary num, index, target - num exist in dictionary, return value
        """
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target - nums[i] == nums[j]:
        #             return [i,j]
        
        # return []
        value_s = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in value_s:
                return [value_s[difference], index]
            
            value_s[value] = index
                 


        