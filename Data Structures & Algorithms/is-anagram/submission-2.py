class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        take string a, first letter, compare it is in string b, and the letter 
        occurs the same number of time

        1. create a dictionary of each letter, and the count in the word
        2. take values in each dict, and compare key exists, and value count is same
        """
        string_s = sorted(s)
        string_t = sorted(t)

        if string_s == string_t:
            return True 

        return False
        
        