class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        connected = 0

        # Build adjacency list
        for i in range(0, n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for n in graph[node]:
                dfs(n)

        for i in range(0, n):
            if i not in visited:
                dfs(i)
                connected += 1

        return connected