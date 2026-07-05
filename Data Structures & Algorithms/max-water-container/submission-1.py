class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, length * height)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea