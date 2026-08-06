class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_len = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                print(i, j)
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    max_len = max(dp[i], max_len)
        
        return max_len