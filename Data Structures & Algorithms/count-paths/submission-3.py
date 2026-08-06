class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def recurse(r, c):
            if r >= m or c >= n:
                return 0

            if r == (m - 1) and c == (n - 1):
                return 1

            if (r, c) in dp:
                return dp[(r, c)]

            res = recurse(r + 1, c) + recurse(r, c + 1)
            dp[(r, c)] = res
            return res

        return recurse(0, 0)