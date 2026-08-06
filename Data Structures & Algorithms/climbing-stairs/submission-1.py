class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            # Base conditions
            if i == 0 or i == 1 or i == 2:
                return i

            return dfs(i - 1) + dfs(i - 2)

        return dfs(n)