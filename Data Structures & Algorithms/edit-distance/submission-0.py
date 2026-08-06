class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def core(i, j):
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return core(i + 1, j + 1)
            else:
                res = core(i + 1, j)
                res = min(res, core(i, j + 1))
                res = min(res, core(i + 1, j + 1))
                return 1 + res

        return core(0, 0)