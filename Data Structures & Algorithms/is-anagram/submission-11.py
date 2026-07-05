class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for c in s:
            freq1[c] = 1 + freq1.get(c, 0)
        for c in t:
            if c not in freq1.keys():
                return False
            freq2[c] = 1 + freq2.get(c, 0) 
        for c in s:
            if c not in freq2.keys():
                return False
            if freq1[c] != freq2[c]:
                return False
        return True
        
        

        