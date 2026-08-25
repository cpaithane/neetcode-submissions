class Solution {
public:
    unordered_map<int, int> dp;

    int dfs(int i, vector<int> &nums) {
        if (i >= nums.size()) {
            dp[i] = 0;
            return 0;
        }

        if (dp.find(i) != dp.end()) {
            return dp[i];
        }

        dp[i] = max((nums[i] + dfs(i + 2, nums)), dfs(i + 1, nums));
        return dp[i];
    }

    int rob(vector<int>& nums) {
        return dfs(0, nums);
    }
};
