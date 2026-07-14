class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 0

        while r < len(prices):
            prof = prices[r] - prices[l]
            maxProfit = max(maxProfit, prof)

            if prices[r] < prices[l]:
                l = r
            r += 1

        return maxProfit
