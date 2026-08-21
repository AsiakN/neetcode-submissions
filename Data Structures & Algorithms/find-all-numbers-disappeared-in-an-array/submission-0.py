class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        the list should be the integers from 1 to len(nums)
        check that i is in nums, if it isn't, return that valus
        """
        list_n = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                list_n.append(i)
        
        return list_n
            
