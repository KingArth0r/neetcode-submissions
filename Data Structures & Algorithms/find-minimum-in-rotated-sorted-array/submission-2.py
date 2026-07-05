class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[l] or len(nums) == 1:
            return nums[l]
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        return nums[r + 1]
        