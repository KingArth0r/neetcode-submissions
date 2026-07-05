class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum():
                if l + 1 >= r:
                    return True
                l += 1
            while not s[r].isalnum():
                if r - 1 < l:
                    return True
                r -= 1
            print(s[l], s[r])
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        