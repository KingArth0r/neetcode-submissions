class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        # if equal then we know it doesn't exist
        while l < r:
            # avoid overflow
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid
            elif nums[mid] <= target:
                l = mid + 1
        return l - 1 if (l and nums[l - 1] == target) else -1
 
        