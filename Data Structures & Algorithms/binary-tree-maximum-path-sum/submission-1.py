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

        # Store the final result in res.
        res = root.val

        def postorder(root):
            nonlocal res
            if root == None:
                return 0

            #
            # Path is considered as follows:
            #      root
            #     /     \
            #   Left    Right
            # So, in this case, find max among left subtree.
            # Find max among right subtree and discard sums which are negative.
            # Sum of left_max, right_max and root.val becomes the sum of path
            # But, return root.val + max(left_max, right_max) to the parent
            # as we need to consider the max sum path.
            lm = postorder(root.left)
            rm = postorder(root.right)
            lm = max(0, lm)
            rm = max(0, rm)

            res = max(res, (lm + rm + root.val))
            return root.val + max(lm, rm)

        postorder(root)
        return res