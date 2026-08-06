class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # DP Solution -> S : O(n^2), T : O(n^3)
        nums = [1] + nums + [1]
        dp = {}

        def recurse(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            # Calculate the result later
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += recurse(l, i - 1) + recurse(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return recurse(1, len(nums) - 2)

        # DP Solution -> S : O(n^2), T : O(n * 2^n)
        nums = [1] + nums + [1]
        dp = {}

        def recurse(l, r):
            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]

            max_coins = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += recurse(l, i - 1) + recurse(i + 1, r)
                max_coins = max(max_coins, coins)

            dp[(l, r)] = max_coins
            return max_coins

        return recurse(1, len(nums) - 2)

        # Recursive solution - > T : O(n * 2^n), S : O(n * 2^n)
        # Append 1 at both the ends of input array
        # to avoid checking for corner cases
        nums = [1] + nums + [1]

        def recurse(nums):
            if len(nums) == 2:
                return 0

            # Calculate max_coins by bursting the current coin
            max_coins = 0
            for i in range(1, len(nums) - 1):
                coins = nums[i - 1] * nums[i] * nums[i + 1]
                coins += recurse(nums[:i] + nums[i+1:])
                max_coins = max(max_coins, coins)

            return max_coins

        return recurse(nums)