class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [-1] * (amount + 1)

        def coinChangeCore(amount):
            if amount == 0:
                return 0

            if dp[amount] != -1:
                return dp[amount]

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + coinChangeCore(amount - coin))
            
            dp[amount] = res
            return dp[amount]

        res = coinChangeCore(amount)
        if res == float("inf"):
            return -1
        return res
