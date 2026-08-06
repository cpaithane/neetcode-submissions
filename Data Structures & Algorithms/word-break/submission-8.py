class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        def recurse(i):
            if i in dp:
                return dp[i]

            for word in wordDict:
                if ((i + len(word)) <= len(s) and s[i : i + len(word)] == word):
                    if recurse(i + len(word)):
                        dp[i] = True
                        return True

            dp[i] = False
            return False

        return recurse(0)

        def recurse(i):
            if i == len(s):
                return True

            for word in wordDict:
                if ((i + len(word)) <= len(s) and s[i : i + len(word)] == word):
                    if recurse(i + len(word)):
                        return True

            return False

        return recurse(0)
