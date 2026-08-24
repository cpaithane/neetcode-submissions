class Solution {
public:
    unordered_map<int, int> dp;

    int dfs(int idx, vector<int> &cost) {

        if (idx >= cost.size()) {
            dp[idx] = 0;
            return 0;
        }

        if (dp.find(idx) != dp.end()) {
            return dp[idx];
        }

        dp[idx] = cost[idx] + min(dfs(idx + 1, cost), dfs(idx + 2, cost));
        return dp[idx];
    }

    int minCostClimbingStairs(vector<int>& cost) {
        return (min(dfs(0, cost), dfs(1, cost)));
    }
};
