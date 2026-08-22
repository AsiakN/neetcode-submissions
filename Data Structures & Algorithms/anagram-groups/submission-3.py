class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        """
        for each string, sort it, and assign it to the key. return all the dictionaries
        """
        new_strs = {}
        new_list = []
        for i in range(len(strs)):
            sorted_s  = ''.join(sorted(strs[i]))
            if new_strs.get(sorted_s):
                new_strs[sorted_s].append(strs[i])
            else:
                new_strs[sorted_s] = [strs[i]]
        
        return (list(new_strs.values()))
            

