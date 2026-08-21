class Solution {
public:
    vector<vector<int>> res;
    vector<int> sub_res;

    void backtrack(int i, vector<int> &nums) {
        if (i >= nums.size()) {
            res.push_back(sub_res);
            return;
        }

        sub_res.push_back(nums[i]);
        backtrack(i+1, nums);
        sub_res.pop_back();
        backtrack(i+1, nums);
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        backtrack(0, nums);
        return res;        
    }
};
