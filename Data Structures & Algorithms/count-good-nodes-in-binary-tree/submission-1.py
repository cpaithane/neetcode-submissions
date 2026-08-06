# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        max_val = -math.inf

        def dfs(root, max_val):
            nonlocal good

            if root == None:
                return

            if root.val >= max_val:
                good += 1
                max_val = max(root.val, max_val)

            if root.left != None:
                dfs(root.left, max_val)

            if root.right != None:
                dfs(root.right, max_val)

        dfs(root, max_val)
        return good