class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        count_dict = {}
        result = 0
        for r in range(len(s)):
    
            # update count for each letter
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1

            # check the range is valid
            if (r-l+1) - max(count_dict.values()) > k:
                count_dict[s[l]] -= 1
                l += 1
            result = max(result, r-l+1 )
        
        return result