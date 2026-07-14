class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        mp = {}
        for r in range(len(s)):
            if s[r] in mp:
                # found dupe, move l to space after,
                # don't move backward
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
        