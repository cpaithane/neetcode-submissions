class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        negative = False
        if x < 0:
            negative = True

        x = abs(x)
        while x != 0:
            digit = x % 10
            x = x // 10
            print(digit, x)

            res = digit + res * 10

        if negative:
            res = -1 * res

        min_int = -1 * (1 << 31)
        max_int = (1 << 31) - 1

        if res > min_int and res < max_int:
            return res
        else:
            return 0