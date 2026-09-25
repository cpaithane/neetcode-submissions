class Solution {
private:
    unordered_map<int, int> dp1;
    unordered_map<int, int> dp2;
    int houses;

    int rob_core(int start, unordered_map<int, int> &dp,
                 bool flag, vector<int>& nums) {
        if (start >= houses ||
            flag == true && start == (houses - 1)) {
            return 0;
        }

        if (dp.find(start) != dp.end()) {
            return dp[start];
        }

        dp[start] = max(nums[start] + rob_core(start + 2, dp, flag, nums),
                        rob_core(start + 1, dp, flag, nums));
        return dp[start];
    }

public:
    int rob(vector<int>& nums) {
        houses = nums.size();
        if (houses == 1) {
            return nums[0];
        }

        return max(rob_core(0, dp1, true, nums),
                   rob_core(1, dp2, false, nums));
    }
};
