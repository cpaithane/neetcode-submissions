class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0
        for num in nums:
            xor = xor ^ num

        for i in range(0, n + 1):
            print(i)
            xor = xor ^ i

        return xor