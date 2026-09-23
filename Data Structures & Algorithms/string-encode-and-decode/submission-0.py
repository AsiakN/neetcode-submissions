class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        In encoding the string, we add the length of the string
        as the first character and then add the separator. Such that 
        on decode, we can get how many character per each word, and 
        where each word begins
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        """
        On decode, we identify the start of each word by checking to 
        see a special symbol exist(#), and then taking the previous
        character which will be the number of letters in that word.
        """
        res, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            res.append(s[j+1:j + 1 + length])

            i = j+1+length
        
        return res

