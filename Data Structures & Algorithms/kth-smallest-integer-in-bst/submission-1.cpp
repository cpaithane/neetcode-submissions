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
    int kth_smallest = INT_MAX;
    int counter = 0;
public:
    void inorder(TreeNode *root, int k) {
        if (root == nullptr) {
            return;
        }

        inorder(root->left, k);

        counter++;
        if (counter == k) {
            kth_smallest = root->val;
            return;
        }

        inorder(root->right, k);
    }

    int kthSmallest(TreeNode* root, int k) {
        inorder(root, k);
        return kth_smallest;
    }
};
