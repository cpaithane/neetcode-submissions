class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = suf = 0
        n = len(nums)
        res = nums[0]

        # Take multiplication in forward fashion and in backward fashion
        # Choose max in every iteration

        def multiply(num, multiplier):
            if multiplier == 0:
                multiplier = 1

            return num * multiplier

        for i in range(n):
            pre = multiply(nums[i], pre)
            suf = multiply(nums[n - i - 1], suf)
            res = max(res, max(pre, suf))

        return res