class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(i):
            # Base condition
            if i >= len(nums):
                return 0

            # If the solution of ith is calculated, return
            if dp[i] != -1:
                return dp[i]

            # Choose maximum of (current house and next to next house or
            # next house) to rob
            # Recurrence relationship
            dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return dp[i]

        # Always, start from 0th house.
        return dfs(0)