# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        md = 0

        # For any given node, the longest path that passes through it
        # is the sum of the height of its left subtree and the height
        # of its right subtree.
        def traversal(root):
            nonlocal md
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return 1

            # Traverse post-order way
            lh = traversal(root.left)
            rh = traversal(root.right)

            # Diameter of the tree is sum of height of left and right subtrees
            md = max(lh + rh, md)

            # What is the height of the subtree?
            # 1 + max(height(l) + height(r))
            return 1 + max(lh, rh)

        traversal(root)
        return md
