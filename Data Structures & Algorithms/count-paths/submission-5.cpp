class Solution {
private:
    map<pair<int, int>, int> dp;
    int rows, cols;

    int recurse(int r, int c) {
        if (r >= rows || c >= cols) {
            return 0;
        }

        if (dp.find({r, c}) != dp.end()) {
            return dp[{r, c}];
        }

        if (r == (rows - 1) && c == (cols - 1)) {
            dp[{r, c}] = 1;
            return 1;
        }

        int res = recurse(r + 1, c) +
                  recurse(r, c + 1);
        dp[{r, c}] = res;
        return res;
    }

public:
    int uniquePaths(int m, int n) {
        rows = m, cols = n;

        return recurse(0, 0);
    }
};
