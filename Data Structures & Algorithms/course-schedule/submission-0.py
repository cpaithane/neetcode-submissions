class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = set()

        for c in range(numCourses):
            graph[c] = []

        for pre in prerequisites:
            neighbors = graph.get(pre[1], [])
            neighbors.append(pre[0])
            graph[pre[1]] = neighbors

        def dfs(node):
            if node in visited:
                return True

            visited.add(node)
            for n in graph[node]:
                if dfs(n):
                    return True
            
            visited.remove(node)
            graph[node] = []
            return False

        count = 0
        for node, neighbors in graph.items():
            if dfs(node):
                return False

            count += 1

        if count == numCourses:
            return True
        return False