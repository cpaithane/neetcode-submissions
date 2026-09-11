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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res_list;
        unordered_map<int, vector<int>> levels;
        queue<pair<TreeNode *, int>> q;

        if (root == nullptr) {
            return res_list;
        }

        q.push({root, 0});
        while (q.empty() == false) {
            pair<TreeNode *, int> p = q.front();
            TreeNode *node = p.first;
            int level = p.second;
            q.pop();

            if (node->left != nullptr) {
                q.push({node->left, level + 1});
            }
            if (node->right != nullptr) {
                q.push({node->right, level + 1});
            }

            vector<int> sub_list = levels[level];
            sub_list.push_back(node->val);
            levels[level] = sub_list;
        }

        for (int i = 0; i < levels.size(); i++) {
            res_list.push_back(levels[i]);
        }
        return res_list;
    }
};
