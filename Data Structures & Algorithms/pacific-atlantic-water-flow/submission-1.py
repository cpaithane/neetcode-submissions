class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        res_list = []

        def dfs(r, c, visited, prev_height):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Idea here is to do dfs in reverse fashion.
        # Start from pacific and atlantic border
        # Add the (r,c) in these sets if prevHeights is greater than or equal
        # to current height
        for c in range(0, cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows-1][c])

        for r in range(0, rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        # Check nodes which are in both sets.
        for r in range(0, rows):
            for c in range(0, cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res_list.append([r, c])

        return res_list