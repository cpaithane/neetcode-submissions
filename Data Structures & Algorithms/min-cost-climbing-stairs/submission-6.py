class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        dp[len(cost)] = 0

        def recurse(i):
            if i >= len(cost):
                return 0

            if i in dp:
                return dp[i]

            res = cost[i] + min(recurse(i + 1), recurse(i + 2))
            dp[i] = res
            return res

        return min(recurse(0), recurse(1))