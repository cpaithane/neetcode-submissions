class Solution {
private:
    unordered_map<int, bool> dp;

    bool recurse(int i, string &s, vector<string>& wordDict) {
        if (i >= s.size()) {
            dp[i] = true;
            return true;
        }

        if (dp.find(i) != dp.end()) {
            return dp[i];
        }

        for (string &word : wordDict) {
            if (i + word.size() <= s.size() &&
                word == s.substr(i, word.size())) {
                if (recurse(i + word.size(), s, wordDict) == true) {
                    dp[i] = true;
                    return true;
                }
            }
        }

        dp[i] = false;
        return false;
    }

public:
    bool wordBreak(string s, vector<string>& wordDict) {
        return recurse(0, s, wordDict);
    }
};
