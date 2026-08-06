class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        def recurse(i):
            if dp[i] == True:
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
