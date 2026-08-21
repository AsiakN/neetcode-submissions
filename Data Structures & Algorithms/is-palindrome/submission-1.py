class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Brute force
        1. take string, remove spacing, make them lower case, 
        2. and reverse string . compare the strings

        Optimal Solution

        """
        string_s = ''.join(filter(str.isalnum, s.lower()))
        return string_s == string_s[::-1]