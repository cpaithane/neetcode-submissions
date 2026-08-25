class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows, cols;
        int l, r;
        rows = matrix.size();
        cols = matrix[0].size();

        l = 0, r = rows * cols - 1;

        while (l <= r) {
            int m = l + (r - l)/2;
            int row = m / cols;
            int col = m % cols;

            if (matrix[row][col] < target) {
                l = m + 1;
            } else if (matrix[row][col] > target) {
                r = m - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
