class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[(l + 1):(r + 1)]) or isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True
