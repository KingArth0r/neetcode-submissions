class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        holding_cell = nums[-k:]
        i = len(nums) - 1
        while i >= k:
            nums[i] = nums[i - k]
            i -= 1
        for i in range(k):
            nums[i] = holding_cell[i]
            
