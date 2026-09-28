class Solution {
private:
    int dfs(int i, string &s, unordered_map<int, int> &dp) {
        int res = 0;
        if (dp.find(i) != dp.end()) {
            return dp[i];
        }

        if (i >= s.size()) {
            dp[i] = 1;
            return 1;
        }

        if (s[i] == '0') {
            dp[i] = 0;
            return 0;
        }

        res = dfs(i + 1, s, dp);

        // Securely validate double-digit boundaries between 10 and 26.
        if (i + 1 < s.size()) {
            if (s[i] == '1' || (s[i] == '2' && s[i + 1] <= '6')) {
                res += dfs(i + 2, s, dp);
            }
        }

        dp[i] = res;
        return res;
    }

public:
    int numDecodings(string s) {
        unordered_map<int, int> dp(s.size() + 1);
        dp[s.size() + 1] = 1;
        return dfs(0, s, dp);
    }
};
