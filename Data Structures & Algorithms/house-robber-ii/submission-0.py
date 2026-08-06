class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 1:
            return nums[0]

        dp1 = [-1] * houses
        dp2 = [-1] * houses

        def robCore(start, dp, flag):
            nonlocal houses
            if ((start >= houses) or
                (flag == True and start == houses - 1)):
                return 0

            if dp[start] != -1:
                return dp[start]

            dp[start] = max(nums[start] + robCore(start + 2, dp, flag),
                            robCore(start + 1, dp, flag))
            return dp[start]

        return max(robCore(0, dp1, True), robCore(1, dp2, False))