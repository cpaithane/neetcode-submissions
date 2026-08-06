class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num

        if total % 2 == 1:
            return False

        def recurse(i, t):
            # Base cases
            if i >= len(nums):
                return t == 0

            if t < 0:
                return False

            return (recurse(i + 1, t) or recurse(i + 1, t - nums[i]))

        return recurse(0, total // 2)