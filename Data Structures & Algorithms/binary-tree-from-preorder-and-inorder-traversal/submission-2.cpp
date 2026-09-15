/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    TreeNode *root = nullptr;
    int pre_idx = 0;

public:
    TreeNode *build_tree_core(vector<int> &preorder,
                              vector<int> &inorder,
                              unordered_map<int, int> &in_dict,
                              int left, int right) {
        if (left < 0 || right > preorder.size() || left > right) {
            return nullptr;
        }

        int val = preorder[pre_idx];
        pre_idx++;
        TreeNode *node = new TreeNode(val);
        if (root == nullptr) {
            root = node;
        }
        
        int idx = in_dict[val];
        node->left = build_tree_core(preorder, inorder, in_dict, left, idx - 1);
        node->right = build_tree_core(preorder, inorder, in_dict, idx + 1, right);
        return node;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        unordered_map<int, int> in_dict;

        for (int i = 0; i < preorder.size(); i++) {
            in_dict[inorder[i]] = i;
        }

        build_tree_core(preorder, inorder, in_dict, 0, preorder.size() - 1);
        return root;
    }
};
