class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i):
            # Base conditions
            if i == 0 or i == 1 or i == 2:
                dp[i] = i
                return i

            if i in dp:
                return dp[i]

            dp[i] = dfs(i - 1) + dfs(i - 2)
            return dp[i]

        return dfs(n)