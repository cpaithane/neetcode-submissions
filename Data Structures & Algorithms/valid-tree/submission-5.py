class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {}
        visited = set()

        # Build adjacency list
        for i in range(0, n):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def is_cycle(node, parent):
            if node in visited:
                return True

            visited.add(node)
            for n in graph[node]:
                if n == parent:
                    continue

                if is_cycle(n, node) == True:
                    return True

            return False

        return is_cycle(0, -1) == False and len(visited) == n