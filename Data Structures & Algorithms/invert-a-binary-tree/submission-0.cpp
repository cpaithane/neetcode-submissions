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
    TreeNode* invertTree(TreeNode* root) {
       /*
        * Use recursion for simple code. Using stack adds complexity in code
        * without much return in saving time and space complexity.
        */
        /* If empty tree. */
        if (root == NULL) {
            return root;
        }
        
        /* Leaf node. */
        if (root->left == NULL && root->right == NULL) {
            return root;
        }

        /*
         * Traverse in post order form.
         */
        TreeNode *left = invertTree(root->left);
        TreeNode *right = invertTree(root->right);

        /* Swap left subtree with right subtree of the root. */
        TreeNode *tmp = left;
        root->left = right;
        root->right = tmp;
        
        /* Return the root. */
        return root;
    }
};
