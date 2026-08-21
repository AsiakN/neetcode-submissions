class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        prevDiff = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                # if prices[i] > prices[j]:
                #     continue
                
                if prices[j] - prices[i] > prevDiff:
                    prevDiff = prices[j] - prices[i]

            if prevDiff > diff:
                diff = prevDiff

        return diff