class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            visited = set()
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            dist = 0

            while q:
                for idx in range(0, len(q)):
                    row, col = q.popleft()

                    if grid[row][col] == 0:
                        return dist

                    for dr, dc in directions:
                        new_row = row + dr                    
                        new_col = col + dc

                        if (new_row < 0 or new_row >= rows or
                            new_col < 0 or new_col >= cols or
                            grid[new_row][new_col] == -1 or
                            (new_row, new_col) in visited):
                            continue

                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))

                dist += 1
            
            return inf

        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r, c)