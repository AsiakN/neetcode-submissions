class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Brute force solution 
        ------------------
        1. find the dictionary of nums, and frequency 
        2. create an array and sort the values
        3. get the values until the len k is reached

        Better solution: 
        -------------------
        1. get dict of num and frequency
        2. use heapq to find the top n keys 

        Bucket sort algorithm : grouping numbers into frequency groups
        e.g all ones go into freq[1], all twos go into freq[2]
        total bucket size will b 
        -----------------------
        1. 
        """
        max_dict = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            max_dict[num] = 1 + max_dict.get(num, 0)
        
        for num, cnt in max_dict.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # arr = []
        # for num, count in max_dict.items():
        #     arr.append([count, num])
        
        # arr.sort()
        
        # res =  []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        
        # return top_keys
