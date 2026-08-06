class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        target = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= target:
                target = i

        return i == target

        # DP
        dp = {}
        def recurse(i):
            if i == len(nums) - 1:
                return True

            if i in dp:
                return dp[i]

            if nums[i] == 0:
                return False

            end = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, end + 1):
                if recurse(j) == True:
                    dp[i] = True
                    return True

            dp[i] = False
            return False

        return recurse(0)

        # Recursive solution
        def recurse(i):
            if i == len(nums) - 1:
                return True

            end = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, end + 1):
                if recurse(j) == True:
                    return True

            return False

        return recurse(0)