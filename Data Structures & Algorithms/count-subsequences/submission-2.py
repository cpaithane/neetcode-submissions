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

