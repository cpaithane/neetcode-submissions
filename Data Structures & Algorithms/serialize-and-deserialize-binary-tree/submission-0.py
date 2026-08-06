# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res_list = []

        def preorder(root):
            nonlocal res_list
            if root == None:
                res_list.append("null")
                return
            else:
                res_list.append(str(root.val))
            
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return ",".join(res_list)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res_list = data.split(",")
        root = None
        pre_idx = 0

        def preorder(res_list):
            nonlocal pre_idx, root
            if res_list[pre_idx] == "null":
                pre_idx += 1
                return None

            node = TreeNode(int(res_list[pre_idx]))
            if root == None:
                root = node
            
            pre_idx += 1
            node.left = preorder(res_list)
            node.right = preorder(res_list)
            return node

        return preorder(res_list)