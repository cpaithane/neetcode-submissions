class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recurse(i):
            if i >= len(cost):
                return 0

            res = cost[i] + min(recurse(i + 1), recurse(i + 2))
            return res

        return min(recurse(0), recurse(1))