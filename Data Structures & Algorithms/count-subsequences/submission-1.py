class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # DP
        dp = {}

        def core(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            res = core(i + 1, j)
            if s[i] == t[j]:
                res += core(i + 1, j + 1)
            
            dp[(i, j)] = res
            return res

        return core(0, 0)

        # Recursive
        def core(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            #
            # There are two cases to match chars.
            # One can skip from s with or without matching chars from t
            # s = caaat
            # t = cat
            # (c)aa(at)
            # (c)a(a)a(t)
            # (ca)aa(t)
            #
            res = core(i + 1, j)
            if s[i] == t[j]:
                res += core(i + 1, j + 1)

            return res

        return core(0, 0)