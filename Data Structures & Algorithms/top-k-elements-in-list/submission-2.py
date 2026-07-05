class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} 
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for num in frequency.keys():
            freq[frequency[num]].append(num)
        res = []
        # loop backwards
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res