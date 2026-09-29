class Solution {
private:
    int sum = 0;
    vector<vector<int>> dp;

    bool recurse(int i, int target, vector<int>& nums) {
        if (i >= nums.size()) {
            return (target == 0);
        }

        if (target < 0) {
            return false;
        }

        if (dp[i][target] != -1) {
            return dp[i][target];
        }

        dp[i][target] = recurse(i + 1, target, nums) ||
                        recurse(i + 1, target - nums[i], nums);
        return dp[i][target];
    }

public:
    bool canPartition(vector<int>& nums) {
        for (int num : nums) {
            sum += num;
        }

        if (sum % 2 == 1) {
            return false;
        }

        int n = nums.size();
        dp = vector<vector<int>>(n, vector<int>((sum / 2) + 1, -1));
        return recurse(0, sum / 2, nums);
    }
};
