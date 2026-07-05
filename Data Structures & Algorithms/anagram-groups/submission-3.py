class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create hash map: 
        # key -> frequency array
        # value -> list of strings with that freq
        # return the list of values

        result = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            result[tuple(freq)].append(s)
        return list(result.values())
        