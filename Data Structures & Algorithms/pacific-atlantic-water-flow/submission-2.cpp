class Solution {
private:
    set<pair<int, int>> pacific;
    set<pair<int, int>> atlantic;
    int rows, cols;

    void dfs(int r, int c,
             set<pair<int, int>> &visited,
             int prev_height,
             vector<vector<int>>& heights) {

        if (r < 0 ||
            r >= rows ||
            c < 0 ||
            c >= cols ||
            visited.find({r, c}) != visited.end() ||
            heights[r][c] < prev_height) {
            return;
        }

        visited.insert({r, c});
        dfs(r + 1, c, visited, heights[r][c], heights);
        dfs(r - 1, c, visited, heights[r][c], heights);
        dfs(r, c + 1, visited, heights[r][c], heights);
        dfs(r, c - 1, visited, heights[r][c], heights);
    }

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        vector<vector<int>> res_list;

        rows = heights.size();
        cols = heights[0].size();

        for (int c = 0; c < cols; c++) {
            dfs(0, c, pacific, heights[0][c], heights);
            dfs(rows - 1, c, atlantic, heights[rows - 1][c], heights);
        }

        for (int r = 0; r < rows; r++) {
            dfs(r, 0, pacific, heights[r][0], heights);
            dfs(r, cols - 1, atlantic, heights[r][cols - 1], heights);
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pacific.find({r, c}) != pacific.end() &&
                    atlantic.find({r, c}) != atlantic.end()) {
                    res_list.push_back({r, c});
                }
            }
        }

        return res_list;
    }
};
