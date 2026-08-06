class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = suf = 0
        n = len(nums)
        res = nums[0]

        for i in range(n):
            multiplier = 1
            if pre != 0:
                multiplier = pre
            
            pre = nums[i] * multiplier

            multiplier = 1
            if suf != 0:
                multiplier = suf

            suf = nums[n - i - 1] * multiplier
            print(pre, suf)
            res = max(res, max(pre, suf))

        return res