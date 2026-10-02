class Solution {
private:
    map<pair<int, int>, bool> dp;

    bool is_interleave(int i, int j, int k,
                       string &s1, string &s2, string &s3) {
        bool res = false;
        if (k == s3.size()) {
            return (i == s1.size() && j == s2.size());
        }

        if (dp.find({i, j}) != dp.end()) {
            return dp[{i, j}];
        }

        if (i < s1.size() && s1[i] == s3[k]) {
            res = is_interleave(i + 1, j, k + 1, s1, s2, s3);
        }

        if (j < s2.size() && s2[j] == s3[k]) {
            res = is_interleave(i, j + 1, k + 1, s1, s2, s3);
        }

        dp[{i, j}] = res;
        return res;
    }

public:
    bool isInterleave(string s1, string s2, string s3) {
        return is_interleave(0, 0, 0, s1, s2, s3);
    }
};
