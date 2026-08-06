"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_dict = {}
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            n_node = Node(node.val, None)
            old_dict[node] = n_node

            for n in node.neighbors:
                dfs(n)

        if node:
            dfs(node)

            for old_node, n_node in old_dict.items():
                for n in old_node.neighbors:
                    n_node.neighbors.append(old_dict[n])

            return old_dict[node]
        return None