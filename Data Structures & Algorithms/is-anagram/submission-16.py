class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #exact same chars <-> number of each char is same
        freq = [0] * 26
        print(ord('a') - 96)
        for c in s:
            freq[ord(c) - 97] += 1
        for c in t:
            freq[ord(c) - 97] -= 1
        for num in freq:
            if num != 0:
                return False
        return True
        