class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP
        dp = []
        num_coins = len(coins)
        coins.sort()

        for c in range(num_coins + 1):
            dp.append([-1] * (amount + 1))

        def changeCore(i, amount):
            if i >= len(coins):
                return 0

            if amount == 0:
                return 1

            if dp[i][amount] != -1:
                return dp[i][amount]

            ways = 0
            if coins[i] <= amount:
                ways = changeCore(i, amount - coins[i])
                ways += changeCore(i + 1, amount)

            dp[i][amount] = ways
            return ways

        ways = changeCore(0, amount)
        return ways

        # Recursion
        if len(coins) == 0:
            return 0

        def changeCore(i, amount):
            if i >= len(coins):
                return 0

            if amount == 0:
                return 1

            ways = 0
            if amount >= coins[i]:
                ways = changeCore(i, amount - coins[i])
                ways += changeCore(i + 1, amount)

            return ways

        ways = changeCore(0, amount)
        return ways