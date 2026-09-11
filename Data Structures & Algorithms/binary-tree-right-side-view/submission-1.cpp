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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res_list;
        queue<pair<TreeNode *, int>> q;
        unordered_map<int, vector<int>> levels;

        if (root == nullptr) {
            return res_list;
        }

        q.push({root, 0});

        while (q.empty() != true) {
            auto [node, level] = q.front();

            if (node->left != nullptr) {
                q.push({node->left, level + 1});
            }
            if (node->right != nullptr) {
                q.push({node->right, level + 1});
            }
            q.pop();

            vector<int> l_list = levels[level];
            l_list.push_back(node->val);
            levels[level] = l_list;
        }

        for (int i = 0; i < levels.size(); i++) {
            vector<int> l_list = levels[i];
            res_list.push_back(l_list[l_list.size() - 1]);
        }

        return res_list;
    }
};
