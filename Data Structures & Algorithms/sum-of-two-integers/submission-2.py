class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff

        while b != 0:
            carry = (a & b) << 1
            # For negative values, a becomes 0 after anding.
            a = (a ^ b) & mask
            b = carry & mask

        # If a is not signed
        if a < 0x7fffffff:
            return a
        else:
            return ~(a ^ mask)