# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root == None:
                return (True, 0)

            l_bal, l_h = dfs(root.left)
            r_bal, r_h = dfs(root.right)

            is_bal = (l_bal and r_bal) and (abs(l_h - r_h) <= 1)
            return (is_bal, 1 + max(l_h, r_h))

        is_bal, h = dfs(root)
        return is_bal