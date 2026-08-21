class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Brute force
        1. take string, remove spacing, make them lower case, remove non-alphas 
        2. and reverse string . compare the strings

        Optimal Solution
        1. initialize two pointers on opposite ends 
        2. move left pointer inward, and check against right pointer also moving
        3. if non-alpha, skip, and increment left. decrement right pointer
        4. if any letter compare is not equal return false; not-palindrome
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isAlphanum(s[l]):
                l += 1
            while r > l and not self.isAlphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l+1, r-1 
        
        return True
    
    def isAlphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

        