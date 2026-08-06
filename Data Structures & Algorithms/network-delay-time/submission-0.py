from heapq import heapify, heappush, heappop 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's shortest path algorithm will solve this.

        # Build adjacency list of directed graph
        graph = {}
        for i in range(0, n + 1):
            graph[i] = []

        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))

        # Use min_heap to store weights and node.
        min_heap = []
        heapify(min_heap)
        heappush(min_heap, (0, k))
        visited = set()
        t = 0

        while min_heap:
            w, node = heappop(min_heap)
            if node in visited:
                continue

            visited.add(node)
            t = w

            # Push all adjacent nodes in min_heap
            for node2, w2 in graph[node]:
                if node2 not in visited:
                    heappush(min_heap, ((w + w2), node2))

        if len(visited) == n:
            return t
        return -1