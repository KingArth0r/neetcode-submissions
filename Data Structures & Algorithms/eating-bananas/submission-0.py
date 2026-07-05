class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            m = l + (r - l) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / m)
            if time <= h:
                #fast enough, see if we can go faster
                res = m
                r = m - 1
            else:
                # too slow, check faster
                l = m + 1
        return res