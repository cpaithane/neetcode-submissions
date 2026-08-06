class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        min_left = prices[0]

        for price in prices:
            min_left = min(min_left, price)
            max_profit = max(max_profit, price - min_left)

        return max_profit

        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r

            r += 1

        return max_profit