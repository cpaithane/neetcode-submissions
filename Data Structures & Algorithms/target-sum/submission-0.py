class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Recursive solution
        def core(i, total):
            if total == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            return core(i + 1, total + nums[i]) + core(i + 1, total - nums[i])

        return core(0, 0)
