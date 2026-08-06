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
            continue

            multiplier = 1
            if pre != 0:
                multiplier = pre
            
            pre = nums[i] * multiplier

            multiplier = 1
            if suf != 0:
                multiplier = suf

            suf = nums[n - i - 1] * multiplier
            res = max(res, max(pre, suf))

        return res