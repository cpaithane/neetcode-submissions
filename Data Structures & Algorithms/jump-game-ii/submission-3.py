class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy, use bfs
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            res += 1
            # Update next window. left as right + 1 and right as farthest
            left = right + 1
            right = farthest

        return res

        # Recursive
        dp = {}
        def recurse(i):
            if i == len(nums) - 1:
                return 0

            if nums[i] == 0:
                dp[i] = float("inf")
                return float('inf')

            if i in dp:
                return dp[i]

            end = min(len(nums) - 1, i + nums[i])
            res = float('inf')

            for j in range(i + 1, end + 1):
                res = min(res, 1 + recurse(j))

            dp[i] = res
            return res

        return recurse(0)
