class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def maxProfitCore(i, buying):
            # Base case
            if i >= len(prices):
                return 0

            # If cached, return the cached value
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                # Choice to buy or cool down
                buy_profit = maxProfitCore(i + 1, not buying) - prices[i]
                cool_profit = maxProfitCore(i + 1, buying)
                dp[(i, buying)] = max(buy_profit, cool_profit)
            else:
                # Choice to sell or cool down
                sell_profit = maxProfitCore(i + 2, not buying) + prices[i]
                cool_profit = maxProfitCore(i + 1, buying)
                dp[(i, buying)] = max(sell_profit, cool_profit)

            return dp[(i, buying)]

        return maxProfitCore(0, True)