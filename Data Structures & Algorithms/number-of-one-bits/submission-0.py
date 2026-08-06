class Solution:
    def hammingWeight(self, n: int) -> int:
        nr_set = 0

        while n != 0:
            n = n & (n - 1)
            nr_set += 1

        return nr_set