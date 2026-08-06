class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost)
        if i == 1:
            return 0

        total = 0
        while True:
            if i <= 2:
                break

            total += min(cost[i - 1], cost[i - 2])
            if cost[i - 1] < cost[i - 2]:
                i = i - 1
            else:
                i = i - 2

        if i == 2:
            total += min(cost[0], cost[1])

        return total

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
