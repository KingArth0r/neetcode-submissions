class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key is each number, value is how many times it shows up
        # each bucket is a list containing each element which occurs i times
        # loop backwards until you've gotten k things in your list
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        frequencies = [[] for i in range(len(nums) + 1)]
        for num, count in counts.items():
            frequencies[count].append(num)
        result = []
        for freq in reversed(frequencies):
            for num in freq:
                result.append(num)
                if len(result) == k:
                    return result

        
        
        