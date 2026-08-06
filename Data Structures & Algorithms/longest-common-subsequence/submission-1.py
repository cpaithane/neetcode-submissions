class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP
        dp = {}

        def lcsCore(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + lcsCore(i + 1, j + 1)
            else:
                dp[(i, j)] = max(lcsCore(i + 1, j), lcsCore(i, j + 1))

            return dp[(i, j)]
        
        return lcsCore(0, 0)

        # Recursive
        def lcsCore(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + lcsCore(i + 1, j + 1)
            return max(lcsCore(i + 1, j), lcsCore(i, j + 1))

        return lcsCore(0, 0)