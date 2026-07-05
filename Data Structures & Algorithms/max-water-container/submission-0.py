class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # h = min(heights[i],heights[j])
        # w = j - i (j > i)
        # loop for all pairs i,j keep track of max h*w
        # only get bigger if something higher than h
        result = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                length = right - left
                height = heights[left]
                area = length * height
                result = max(result, area)
                left += 1
            else:
                length = right - left
                height = heights[right]
                area = length * height
                result = max(result, area)
                right -= 1
        return result

        