class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            #skip # symbol
            while s[j] != '#':
                j += 1
            #read number
            length = int(s[i:j])
            # skip over number
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
            
