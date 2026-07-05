class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for c in s:
            if c in letters.keys():
                letters[c] += 1
            else:
                letters[c] = 1
        for c in t:
            if c not in letters.keys():
                return False
            else:
                letters[c] -= 1
        for c in s:
            if letters[c] != 0:
                return False
        return True

        