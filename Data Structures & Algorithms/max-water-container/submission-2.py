class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        
        """
        # Brute force 
        # ------------------------------------------->
        # totalArea = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         height = min(heights[j], heights[i])
        #         width = j-i
        #         area = height * width
        #         if area > totalArea:
        #             totalArea = area
        
        # return totalArea

        #Optimal solution 
        l, r = 0, len(heights)-1
        totalArea = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l 
            area = height * width
            if area > totalArea:
                totalArea = area 
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return totalArea


