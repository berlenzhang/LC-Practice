import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_h = r

        while l <= r:
            mid = (l + r) // 2
            hrs = 0
            for i in piles:
                hrs += math.ceil(i / mid)
            if hrs <= h:
                r = mid - 1
                min_h = mid
            else:
                l = mid + 1
        
        return min_h