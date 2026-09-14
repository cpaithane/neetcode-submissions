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
    int good = 0;

public:
    void goodNodesCore(TreeNode *root, int max_val) {
        if (root == nullptr) {
            return;
        }

        if (root->val >= max_val) {
            good++;
            max_val = max(root->val, max_val);
        }

        if (root->left != nullptr) {
            goodNodesCore(root->left, max_val);
        }

        if (root->right != nullptr) {
            goodNodesCore(root->right, max_val);
        }
    }

    int goodNodes(TreeNode* root) {
        int max_val = INT_MIN;
        goodNodesCore(root, max_val);
        return good;
    }
};
