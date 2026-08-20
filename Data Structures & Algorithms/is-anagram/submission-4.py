class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        take string a, first letter, compare it is in string b, and the letter 
        occurs the same number of time

        1. create a dictionary of each letter, and the count in the word
        2. take values in each dict, and compare key exists, and value count is same
        """
        if len(s) != len(t):
            return False
        
        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
        
        return hash_s == hash_t
        