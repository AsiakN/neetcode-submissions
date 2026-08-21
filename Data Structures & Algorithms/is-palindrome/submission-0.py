class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. take string, remove spacing, make them lower case, 
        2. and reverse string . compare the strings
        """
        string_s = ''.join(filter(str.isalnum, s.lower()))
        reversed_s = ''.join(reversed(string_s))

        return string_s == reversed_s