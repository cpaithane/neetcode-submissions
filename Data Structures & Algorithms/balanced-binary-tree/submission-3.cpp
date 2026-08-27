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
    bool dfs(TreeNode *root, int &h) {
        int lh = 0;
        int rh = 0;

        if (root == nullptr) {
            return true;
        }

        bool l_balanced = dfs(root->left, lh);
        bool r_balanced = dfs(root->right, rh);
        h = 1 + max(lh, rh);

        if (l_balanced && r_balanced && (abs(lh - rh) <= 1)) {
            return true;
        } else {
            return false;
        }

    }

    bool isBalanced(TreeNode* root) {
        int h = 0;
        return dfs(root, h);
    }
};
