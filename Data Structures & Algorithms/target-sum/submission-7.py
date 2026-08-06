class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP
        dp = {}

        def core(i, total):
            if i == len(nums):
                return total == target

            if (i, total) in dp:
                return dp[(i, total)]

            res = core(i + 1, total + nums[i]) + core(i + 1, total - nums[i])
            dp[(i, total)] = res
            return res

        return core(0, 0)

        # Recursive solution
        def core(i, total):
            if total == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            return core(i + 1, total + nums[i]) + core(i + 1, total - nums[i])

        return core(0, 0)