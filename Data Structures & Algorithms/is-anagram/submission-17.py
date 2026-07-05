class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c in s:
            freq1[ord(c) - ord('a')] += 1
        for c in t:
            freq2[ord(c) - ord('a')] += 1
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True
