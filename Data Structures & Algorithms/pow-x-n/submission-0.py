class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        negative = False
        if n < 0:
            negative = True

        power = abs(n)
        while power != 0:
            if power % 2 == 1:
                res = res * x

            x = x * x
            power = power // 2

        if negative == True:
            res = 1 / res

        return res