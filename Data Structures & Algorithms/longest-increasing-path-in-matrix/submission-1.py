class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # DP solution
        dp = {}

        def recurse(i, j, prev):
            if (i < 0 or i >= len(matrix) or 
                j < 0 or j >= len(matrix[0]) or
                prev >= matrix[i][j]):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            dist = 1 + recurse(i + 1, j, matrix[i][j])
            dist = max(dist, 1 + recurse(i - 1, j, matrix[i][j]))
            dist = max(dist, 1 + recurse(i, j + 1, matrix[i][j]))
            dist = max(dist, 1 + recurse(i, j - 1, matrix[i][j]))

            dp[(i, j)] = dist
            return dist

        # Recursive solution m * n * 4^(m*n)
        def recurse(i, j, prev):
            if (i < 0 or i >= len(matrix) or 
                j < 0 or j >= len(matrix[0]) or
                prev >= matrix[i][j]):
                return 0

            dist = 1 + recurse(i + 1, j, matrix[i][j])
            dist = max(dist, 1 + recurse(i - 1, j, matrix[i][j]))
            dist = max(dist, 1 + recurse(i, j + 1, matrix[i][j]))
            dist = max(dist, 1 + recurse(i, j - 1, matrix[i][j]))

            return dist

        dist = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dist = max(dist, recurse(i, j, float("-inf")))

        return dist