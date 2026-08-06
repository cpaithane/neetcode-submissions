# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        max_val = math.inf
        min_val = -math.inf

        def check_valid(root, min_val, max_val):
            if root == None:
                return True

            if not (min_val < root.val and root.val < max_val):
                return False

            return check_valid(root.left, min_val, root.val) and check_valid(root.right, root.val, max_val)

        return check_valid(root, min_val, max_val)
