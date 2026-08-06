class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)
        dp[len(s)] = 1

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            if s[i] == "0":
                return 0

            res1 = dfs(i+1)
            res2 = 0
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                res2 = dfs(i + 2)

            dp[i] = res1 + res2
            return dp[i]

        return dfs(0)

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
                ):
                res += dfs(i + 2)

            dp[i] = res
            return dp[i]

        return dfs(0)