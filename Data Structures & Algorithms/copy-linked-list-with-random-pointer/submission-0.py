"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        idx_dict = {None:None}

        tmp = head
        while tmp:
            new_node = Node(tmp.val, None, None)
            idx_dict[tmp] = new_node
            tmp = tmp.next

        tmp = head
        while tmp:
            new_node = idx_dict[tmp]
            new_node.next = idx_dict[tmp.next]
            new_node.random = idx_dict[tmp.random]
            tmp = tmp.next
        
        return idx_dict[head]
