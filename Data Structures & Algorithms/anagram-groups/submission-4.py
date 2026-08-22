class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        """
        for each string, sort it, and assign it to the key. return all the dictionaries
        """
        new_strs = defaultdict(list)
        for s in strs:
            sorted_s  = ''.join(sorted(s))
            new_strs[sorted_s].append(s)
        
        return (list(new_strs.values()))
            

