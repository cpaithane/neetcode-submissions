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

        def dfs(node):
            if node in old_dict:
                return old_dict[node]

            n_node = Node(node.val, None)
            old_dict[node] = n_node

            for n in node.neighbors:
                n_node.neighbors.append(dfs(n))

            return n_node

        if node:
            return dfs(node)
        return None