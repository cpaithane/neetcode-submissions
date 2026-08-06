class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        cur_size = 0
        max_size = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            nonlocal cur_size
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                (r, c) in visited):
                return

            visited.add((r, c))
            cur_size += 1
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for r in range(0, rows):
            for c in range(0, cols):
                dfs(r, c)
                max_size = max(max_size, cur_size)
                cur_size = 0

        return max_size