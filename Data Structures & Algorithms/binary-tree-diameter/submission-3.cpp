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
    int dfs(TreeNode *root, int &md) {
        if (root == nullptr) {
            return 0;
        }        

        if (root->left == nullptr && root->right == nullptr) {
            return 1;
        }

        int lh = dfs(root->left, md);
        int rh = dfs(root->right, md);

        md = max(lh + rh, md);
        return 1 + max(lh, rh);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        int md = 0;
        dfs(root, md);
        return md;
    }
};
