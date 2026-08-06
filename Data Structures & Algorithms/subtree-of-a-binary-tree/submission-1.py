# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # subTree is exhausted, then return True
        if subRoot == None:
            return True
        
        # The root is exhausted before subRoot, return False
        if root == None:
            return False

        # Structure is same, return True
        if self.isSameTree(root, subRoot):
            return True

        # Go for left first. If not found, go for right.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True

        if root == None or subRoot == None:
            return False

        if (root.val == subRoot.val) and (self.isSameTree(root.left, subRoot.left)) and (self.isSameTree(root.right, subRoot.right)):
            return True

        return False