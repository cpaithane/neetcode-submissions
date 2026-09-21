class Solution {
private:
    set<pair<int, int>> visited;
    int max_area, cur_area;

public:
    void dfs(int r, int rows, int c, int cols, vector<vector<int>>& grid) {
        if (r < 0 ||
            c < 0 ||
            r >= rows ||
            c >= cols ||
            visited.find({r, c}) != visited.end() ||
            grid[r][c] == 0) {
                return;
            }

        visited.insert({r, c});
        cur_area++;

        dfs(r + 1, rows, c, cols, grid);
        dfs(r - 1, rows, c, cols, grid);
        dfs(r, rows, c + 1, cols, grid);
        dfs(r, rows, c - 1, cols, grid);
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        max_area = cur_area = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                dfs(r, rows, c, cols, grid);
                max_area = max(max_area, cur_area);
                cur_area = 0;
            }
        }

        return max_area;
    }
};
