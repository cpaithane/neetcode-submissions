class Solution {
private:
    map<pair<int, int>, int> dp;

    int find_target_core(int i, int total, vector<int>& nums, int target) {
        int res;

        if (total == target && i == nums.size()) {
            return 1;
        }

        if (i >= nums.size()) {
            return 0;
        }

        if (dp.find({i, total}) != dp.end()) {
            return dp[{i, total}];
        }

        res = find_target_core(i + 1, total + nums[i], nums, target) +
              find_target_core(i + 1, total - nums[i], nums, target);
        dp[{i, total}] = res;
        return res;
    }

public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return find_target_core(0, 0, nums, target);
    }
};
