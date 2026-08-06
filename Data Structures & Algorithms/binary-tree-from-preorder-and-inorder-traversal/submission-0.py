# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        root = None
        search_dict = {}
        pre_idx = 0

        if n == 0:
            return None

        for i in range(0, len(inorder)):
            search_dict[inorder[i]] = i

        def buildTreeCore(left, right):
            nonlocal preorder
            nonlocal inorder
            nonlocal root
            nonlocal search_dict
            nonlocal n, pre_idx

            if left < 0 or right > n or left > right:
                return None

            print(pre_idx)
            val = preorder[pre_idx]
            pre_idx += 1
            node = TreeNode(val, None, None)
            if root == None:
                root = node
            
            # Search val in inorder
            idx = search_dict.get(val)

            # Elements from 0 -> idx - 1 are part of left subtree
            # Elements from idx -> n - 1 are part of right subtree
            node.left = buildTreeCore(left, idx - 1)
            node.right = buildTreeCore(idx + 1, right)
            return node

        buildTreeCore(0, n-1)
        return root