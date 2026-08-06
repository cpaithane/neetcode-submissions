# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        res_list = []
        level_dict = {}
        level = 0

        if root == None:
            return []

        queue.append((root, level))

        while len(queue) != 0:
            node, level = queue.pop(0)

            level_list = level_dict.get(level, [])
            level_list.append(node.val)
            level_dict[level] = level_list

            if node.left != None:
                queue.append((node.left, level + 1))

            if node.right != None:
                queue.append((node.right, level + 1))

        for level, level_list in level_dict.items():
            res_list.append(level_list[len(level_list) - 1])

        return res_list