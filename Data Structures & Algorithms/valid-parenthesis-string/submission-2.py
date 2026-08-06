class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0

        for ch in s:
            if ch == "(":
                left_min += 1
                left_max += 1
            elif ch == ")":
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1

            # Choice of decrementing left_min is wrong, reset
            if left_min < 0:
                left_min = 0
        
            if left_max < 0:
                return False

        return left_min == 0

        # DP and Recursive
        dp = {}

        def recurse(i, nr_open):
            # Base conditions
            if nr_open < 0:
                return False

            if i == len(s):
                return nr_open == 0

            if (i, nr_open) in dp:
                return dp[(i, nr_open)]

            res = False
            if s[i] == "(":
                res = recurse(i + 1, nr_open + 1)
            elif s[i] == ")":
                res = recurse(i + 1, nr_open - 1)
            else:
                res = (recurse(i + 1, nr_open + 1) or 
                        recurse(i + 1, nr_open - 1) or
                        recurse(i + 1, nr_open))

            dp[(i, nr_open)] = res
            return res

        return recurse(0, 0)