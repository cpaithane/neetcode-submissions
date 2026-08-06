class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        #
        # Init the pre, suff and res lists of n elements with 0
        #
        pre_mult = [0] * n
        suff_mult = [0] * n
        res = [0] * n
        mult = 1
        
        pre_mult[0] = suff_mult[n-1] = 1

        # From 1 to n
        for i in range(1, n):     
            mult = mult * nums[i-1]
            pre_mult[i] = mult

        mult = 1
        # From n-2 to 0
        for i in range(len(nums) - 2, -1, -1):
            mult = mult * nums[i+1]
            suff_mult[i] = mult
        
        for i in range(0, n):
            res[i] = (pre_mult[i] * suff_mult[i])
        
        return res
