class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(0, 32):
            # Find out bit at ith location
            bit = (n >> i) & 1
            # Put this bit at 31 - ith location
            res += (bit << (31 - i))

        return res