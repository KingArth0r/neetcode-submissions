class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #key is each number, value is how many times it shows up
        count = {}
        # each bucket is a list containing each element which occurs i times
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt, in count.items():
            freq[cnt].append(num)

        res = []
        # loop backwards until you've gotten k things in your list
        for item in reversed(freq):
            for num in item:
                res.append(num)
                if len(res) == k:
                    return res 
        
        
        
        