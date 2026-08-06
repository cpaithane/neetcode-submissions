class Solution:
    def jump(self, nums: List[int]) -> int:
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
