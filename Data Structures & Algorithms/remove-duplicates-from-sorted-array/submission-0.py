class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remember we only need the first k elements,
        # the left pointer (index) will keep track of non-duplicates, 
        # the right one will skip duplicates
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l