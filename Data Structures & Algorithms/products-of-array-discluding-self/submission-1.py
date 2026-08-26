class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        for each i, remove, create a new array without that i, and use that
        to multiply
        """
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        