class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Build adjacency list
        # char with set(). set is used because it needs unique set of 
        # adjacent chars
        # Topological sort. If there is cycle, return invalid.

        graph = {}
        for word in words:
            for ch in word:
                graph[ch] = set()

        for i in range (0, len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True

            for n in graph[c]:
                if dfs(n) == True:
                    return True

            visited[c] = False
            res.append(c)
            return False

        for c in graph:
            if dfs(c) == True:
                return ""
        
        res = reversed(res)
        return "".join(res)
