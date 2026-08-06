class Solution:
    def checkValidString(self, s: str) -> bool:
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