class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        dp[len(s)] = True

        def recurse(i):
            # If i position is evaluated, then return that instead of evaluating again
            if i in dp:
                return dp[i]

            # Choose word from dictionary and search in string
            # If found, go for next breaking in string
            for word in wordDict:
                if ((i + len(word)) <= len(s) and s[i : i + len(word)] == word):
                    if recurse(i + len(word)):
                        dp[i] = True
                        return True

            # wordDict is exhausted, return false.
            dp[i] = False
            return False

        return recurse(0)