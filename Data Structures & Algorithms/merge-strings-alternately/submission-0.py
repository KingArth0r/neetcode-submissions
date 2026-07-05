class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        res = ""
        for i in range(min(m, n)):
            res = res + word1[i] + word2[i]
        if m > n:
            res = res + word1[n:]
        elif m < n:
            res = res + word2[m:]
        return res
        