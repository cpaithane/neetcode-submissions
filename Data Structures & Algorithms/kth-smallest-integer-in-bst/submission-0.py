# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = 0
        kth_element = math.inf

        def inorder(root):
            nonlocal visited
            nonlocal kth_element

            if root == None:
                return

            inorder(root.left)

            visited += 1
            if visited == k:
                kth_element = root.val
                return

            inorder(root.right)

        inorder(root)
        return kth_element