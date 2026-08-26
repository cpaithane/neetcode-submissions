class Solution {
private:
    vector<vector<int>> res;
    vector<int> sub_res; 
public:

    void combinationSumCore(vector<int> &nums, int target, int idx, int cur_sum) {

        if (cur_sum == target) {
            res.push_back(sub_res);
            return;
        }

        if (idx >= nums.size() || cur_sum > target) {
            return;
        }

        sub_res.push_back(nums[idx]);
        combinationSumCore(nums, target, idx, cur_sum + nums[idx]);

        sub_res.pop_back();
        combinationSumCore(nums, target, idx + 1, cur_sum);
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        combinationSumCore(nums, target, 0, 0);        
        return res;
    }
};
