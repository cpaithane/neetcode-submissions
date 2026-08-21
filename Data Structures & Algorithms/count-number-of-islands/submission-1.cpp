class Solution {
public:
    void dfs(int r, int c, vector<vector<char>>& grid) {

        if (r < 0 || r >= grid.size() ||
            c < 0 || c >= grid[0].size() ||
            grid[r][c] == '0') {
                return;
            }

        grid[r][c] = '0';
        dfs(r, c - 1, grid);
        dfs(r, c + 1, grid);
        dfs(r + 1, c, grid);
        dfs(r - 1, c, grid);
    }

    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int num_islands = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    num_islands++;
                }
            }
        }

        return num_islands;
    }
};
