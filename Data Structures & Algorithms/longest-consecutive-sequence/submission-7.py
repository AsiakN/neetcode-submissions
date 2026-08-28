class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        #two pointers. while right - left == 1, then update count, increase right pointer, increase left pointer
        # if there is a break, then increase the main left pointer, and set right to something just after it 

        # nums.sort()
        elements = set(nums)
        for num in elements:
            if (num-1) not in elements:
                length = 1
                while (num + length) in elements:
                    length += 1
                    
                count = max(length, count)
        
        return count
            