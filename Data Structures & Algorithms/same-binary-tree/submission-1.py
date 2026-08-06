# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Empty trees
        if p == None and q == None:
            return True

#        print("p", p.val, p.left, p.right)
#        print("q", q.val, q.left, q.right)

        if p == None or q == None:
            return False

        # Structures are not same
        if (p.left != None and q.left == None) or (p.right != None and q.right == None):
            return False

        # values are same and structures are same
        # That means, inorder traversal.
        if (p.val == q.val) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)):
            return True
        
        return False