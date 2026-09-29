class Solution {
private:
    vector<vector<int>> dp;

    int dfs(int i, int j, vector<int>& nums) {
        int lis;

        if (i == nums.size()) {
            return 0;
        }

        if (dp[i][j + 1] != -1) {
            return dp[i][j + 1];
        }
        // exclusion
        lis = dfs(i + 1, j, nums);

        // inclusion
        if (j == -1 || nums[j] < nums[i]) {
            lis = max(lis, 1 + dfs(i + 1, i, nums));
        }

        dp[i][j + 1] = lis;
        return lis;
    }
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        dp = vector<vector<int>>(n, vector<int>(n + 1, -1));
        return dfs(0, -1, nums);
    }
};
