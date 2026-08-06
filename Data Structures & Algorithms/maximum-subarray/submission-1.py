class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        cur_sum = 0
        max_sum = nums[0]

        for num in nums:
            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num
            max_sum = max(max_sum, cur_sum)

        return max_sum

    # DP
    # include nums[i] + dfs(i + 1)
    # Don't include nums[i] + dfs(i + 1)
    #