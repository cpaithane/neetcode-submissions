class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        fresh = 0

        # Add fresh fruit to the queue.
        def add_queue(r, c):
            nonlocal fresh
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 2 or
                grid[r][c] == 0):
                return

            fresh -= 1
            q.append((r, c))
            visited.add((r, c))

        # Store all rotten fruits in a queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Traverse layer by layer
        # Add the fresh fruit to the q every minute.
        mins = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                add_queue(r + 1, c)
                add_queue(r - 1, c)
                add_queue(r, c + 1)
                add_queue(r, c - 1)

            mins += 1
        
        # Check if there is any fresh fruit.
        if fresh == 0:
            return mins
        return -1