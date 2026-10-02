class Solution {
private:
    map<pair<int, int>, int> dp;

    int min_distance_core(int i, int j, string &word1, string &word2) {
        int res = 0;
        if (i == word1.size()) {
            dp[{i, j}] = word2.size() - j;
            return dp[{i, j}];
        }

        if (j == word2.size()) {
            dp[{i, j}] = word1.size() - i;
            return dp[{i, j}];
        }

        if (dp.find({i, j}) != dp.end()) {
            return dp[{i, j}];
        }

        if (word1[i] == word2[j]) {
            res = (min_distance_core(i + 1, j + 1, word1, word2));
        } else {
            res = min(min_distance_core(i + 1, j, word1, word2),
                      min_distance_core(i, j + 1, word1, word2));
            res = 1 + min(res, min_distance_core(i + 1, j + 1, word1, word2));
        }

        dp[{i, j}] = res;
        return res;
    }

public:
    int minDistance(string word1, string word2) {
        return min_distance_core(0, 0, word1, word2);
    }
};
