class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        visited = set()
        cycle = set()
        count = len(edges)

        for i in range(0, count + 1):
            graph[i] = []

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        cycle_start = -1

        def dfs(node, parent):
            nonlocal cycle_start
            # Detection of cycle, track cycle_start
            if node in visited:
                cycle_start = node
                return True

            visited.add(node)

            for n in graph[node]:
                if n == parent:
                    continue

                if dfs(n, node) == True:
                    # cycle_start is valid, add the n to visited
                    if cycle_start != -1:
                        cycle.add(n)
                    
                    # node has reached cycle_start, so break the cycle_start
                    if node == cycle_start:
                        cycle_start = -1

                    return True

            return False

        dfs(1, -1)

        for edge in reversed(edges):
            if edge[0] in cycle and edge[1] in cycle:
                return [edge[0], edge[1]]

        return []