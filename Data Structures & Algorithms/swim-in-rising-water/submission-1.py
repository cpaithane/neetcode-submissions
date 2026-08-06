from heapq import heapify, heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # No need to have adjacency list as matrix is given.
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        min_heap = []
        heapify(min_heap)

        # Always start from (0, 0) with weight of 0
        visited.add((0, 0))
        heappush(min_heap, (max(0, grid[0][0]), (0, 0)))

        def push_heap(r, c, tm):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited):
                return

            visited.add((r, c))
            # Push maximum of time so far and grid's value to heap.
            heappush(min_heap, (max(tm, grid[r][c]), (r, c)))

        while min_heap:
            tm, (r, c) = heappop(min_heap)

            # return time if it reaches bottom, right corner
            if (r == rows - 1) and (c == cols - 1):
                return tm

            # Traverse in 4 directions
            push_heap(r + 1, c, tm)
            push_heap(r - 1, c, tm)
            push_heap(r, c + 1, tm)
            push_heap(r, c - 1, tm)

        return 0