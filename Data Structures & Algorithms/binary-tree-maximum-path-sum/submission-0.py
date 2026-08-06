# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        res = root.val

        def postorder(root):
            nonlocal res
            if root == None:
                return 0

            lm = postorder(root.left)
            rm = postorder(root.right)
            lm = max(0, lm)
            rm = max(0, rm)

            res = max(res, (lm + rm + root.val))
            return root.val + max(lm, rm)

        postorder(root)
        return res