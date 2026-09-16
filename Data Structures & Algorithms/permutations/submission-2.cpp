class Solution {
private:
    vector<vector<int>> res_list;
    vector<int> sub_res;

public:
    void recurse(vector<int> &nums, vector<bool> &visited) {
        if (nums.size() == sub_res.size()) {
            res_list.push_back(sub_res);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (visited[i] == true) {
                continue;
            }

            visited[i] = true;
            sub_res.push_back(nums[i]);
            recurse(nums, visited);

            sub_res.pop_back();
            visited[i] = false;
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> visited(nums.size());
        recurse(nums, visited);
        return res_list;
    }
};
