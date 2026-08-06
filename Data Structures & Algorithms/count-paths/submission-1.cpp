class Solution {
public:
    vector<vector<int>> dp;

    int uniquePathsCore(int r, int c, int m, int n) {
        if ((r == (m - 1)) && (c == (n - 1))) {
            return 1;
        }

        if (r >= m || c >= n) {
            return 0;
        }

        if (dp[r][c] != -1) {return dp[r][c];}

        dp[r][c] = uniquePathsCore(r+1, c, m, n) + uniquePathsCore(r, c+1, m, n);

        return dp[r][c];
    }

    int uniquePaths(int m, int n) {
        dp.resize(m, vector<int>(n, -1));
        return uniquePathsCore(0, 0, m, n);
    }
};
