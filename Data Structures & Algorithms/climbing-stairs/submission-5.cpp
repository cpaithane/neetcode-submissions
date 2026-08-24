class Solution {
public:
    unordered_map<int, int> dp;

    int dfs(int i, int n) {

        if (i >= n) {
            return i == n;
        }

        if (dp.find(i) != dp.end()) {
            return dp[i];
        }

        dp[i] = (dfs(i + 1, n) + dfs(i + 2, n));
        return dp[i];
    }

    int climbStairs(int n) {
        return dfs(0, n);
    }
};
