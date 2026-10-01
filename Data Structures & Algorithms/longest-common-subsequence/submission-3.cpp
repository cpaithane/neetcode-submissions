class Solution {
private:
    map<pair<int, int>, int> dp;

    int lcs_core(int i, int j, string &text1, string &text2) {
        if (i >= text1.size() || j >= text2.size()) {
            return 0;
        }

        if (dp.find({i, j}) != dp.end()) {
            return dp[{i, j}];
        }

        if (text1[i] == text2[j]) {
            dp[{i, j}] = 1 + lcs_core(i + 1, j + 1, text1, text2);
            return dp[{i, j}];
        } else {
            dp[{i, j}] = max(lcs_core(i + 1, j, text1, text2),
                             lcs_core(i, j + 1, text1, text2));
            return dp[{i, j}];
        }
    }

public:
    int longestCommonSubsequence(string text1, string text2) {
        return lcs_core(0, 0, text1, text2);
    }
};
