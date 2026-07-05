class Solution:
    def trap(self, height: List[int]) -> int:
        # find indices all peaks, compute areas between peaks, then sum
        # assume outside is height zero
        # peak if height[i] >= height[i+1], height[i-1]
        # to find area, 
        # for each peak add up difference between height and min peak.
        # use two pointers to keep track of each peak
        
        # find all peaks
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        res = 0
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res     
            
                
            
       