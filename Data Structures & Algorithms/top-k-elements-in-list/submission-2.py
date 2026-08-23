class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Brute force solution 
        ------------------
        1. find the dictionary of nums, and frequency 
        2. create an array and sort the values
        3. get the values until the len k is reached
        """
        max_dict = {}

        for num in nums:
            max_dict[num] = 1 + max_dict.get(num, 0)
        arr = []
        for num, count in max_dict.items():
            arr.append([count, num])
        
        arr.sort()
        
        res =  []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
