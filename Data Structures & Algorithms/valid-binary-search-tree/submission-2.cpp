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
public:
    bool check_valid_bst(TreeNode *root, int min_val, int max_val) {
        if (root == nullptr) {
            return true;
        }

        if (!(min_val < root->val && root->val < max_val)) {
            return false;
        }

        return check_valid_bst(root->left, min_val, root->val) &&
               check_valid_bst(root->right, root->val, max_val);
    }

    bool isValidBST(TreeNode* root) {
        int min_val = INT_MIN;
        int max_val = INT_MAX;
        return check_valid_bst(root, min_val, max_val);
    }
};
