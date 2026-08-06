# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = 0

        def traversal(root):
            nonlocal md
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return 1

            dl = traversal(root.left)
            dr = traversal(root.right)
            md = max(dl + dr, md)

            return 1 + max(dl, dr)

        traversal(root)
        return md
