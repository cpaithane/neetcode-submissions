class Solution {
public:
    unordered_map<int, int> dp;

    int dfs(int i) {

        if (i == 0 || i == 1 || i == 2) {
            dp[i] = i;
            return i;
        }

        if (dp.find(i) != dp.end()) {
            return dp[i];
        }

        dp[i] = dfs(i - 1) + dfs(i - 2);
        return dp[i];
    }

    int climbStairs(int n) {
        return dfs(n);
    }
};
