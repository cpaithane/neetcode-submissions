class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegrees = [0] * numCourses
        q = deque()
        res_list = []

        for c in range(numCourses):
            graph[c] = []

        # Form a graph of depedencies.
        for pre in prerequisites:
            neighbors = graph.get(pre[1], [])
            neighbors.append(pre[0])
            graph[pre[1]] = neighbors
            indegrees[pre[0]] += 1

        for i in range(0, numCourses):
            if indegrees[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res_list.append(node)

            for n in graph[node]:
                indegrees[n] -= 1
                if indegrees[n] == 0:
                    q.append(n)

        if len(res_list) == numCourses:    
            return res_list
        return []