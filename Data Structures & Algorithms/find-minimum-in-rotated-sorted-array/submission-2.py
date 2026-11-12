class Solution:
    def findMin(self, nums: List[int]) -> int: 
        # min_num = math.inf
        # for i in range(len(nums)):
        #     if nums[i] < min_num:
        #         min_num = nums[i]
        # return int(min_num)

        # O(log n) time
        
        # find the midpoint, and check left and right, go with smallest value
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break 
            
            mid = (l+r) // 2 
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1 
        return res 

