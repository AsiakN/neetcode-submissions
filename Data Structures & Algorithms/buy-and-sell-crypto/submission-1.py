class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        brute force: 
        1. Take a buy at index i,
        2. loop over every possible sell date in the future
        3. Find the max difference and return int
        4. repeat until every element

        Optimal Solution: two pointers
        1. buy is left pointer, sell is right pointer( future date)
        2. if buy is lower than sell, then compute profit 
        3. Else move pointer to that day when buy was greater than sell; 
        That is the new lowest. 
        e.g day 1 => 2, day 2 => 4, day 3 => 1 day 5 => 5
        1. day 1; l=0 day 2; r=1 day1 < day2 => profit calculated 
        2. right pointer moves to next day ( day 3)
        3. day 1 > day 3 => new lowest buy 
        4. New buy pointer moves to day 3, sell pointer moves to right 
        5. Process starts again
        """
        maxP = 0 
        l,r = 0,1

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxP = max(maxP, diff)

            else:
                l = r

            r += 1 

        return maxP