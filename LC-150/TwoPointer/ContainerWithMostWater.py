class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            maxWater = max(maxWater, (r - l) * min(heights[r], heights[l]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
        return maxWater
