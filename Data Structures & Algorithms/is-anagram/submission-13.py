class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # strings are anagram iff frequency maps are the same 
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in s:
            freq1[ord(c) - ord('a')] += 1
        for c in t:
            freq2[ord(c) - ord('a')] += 1
        for i in range(len(freq1)):
            if freq1[i] != freq2[i]:
                return False
        return True

        

        