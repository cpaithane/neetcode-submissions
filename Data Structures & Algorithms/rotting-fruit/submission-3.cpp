class Solution {
private:
    int rows, cols, fresh;
    queue<pair<int, int>> q;
    set<pair<int, int>> visited;

    void add_queue(int r, int c, vector<vector<int>>& grid) {
        if (r < 0 ||
            r >= rows ||
            c < 0 ||
            c >= cols ||
            grid[r][c] == 0 ||
            grid[r][c] == 2 ||
            visited.find({r, c}) != visited.end()) {
                return;
            }
        
        q.push({r, c});
        visited.insert({r, c});
        fresh--;
    }

public:
    int orangesRotting(vector<vector<int>>& grid) {
        int mins = 0;
        rows = grid.size();
        cols = grid[0].size();

        fresh = 0;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    q.push({r, c});
                    visited.insert({r, c});
                } else if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }

        while (fresh > 0 && !q.empty()) {
            int level_size = q.size();

            for (int i = 0; i < level_size; i++) {
                auto [r, c] = q.front();
                q.pop();

                grid[r][c] = 2;

                add_queue(r + 1, c, grid);
                add_queue(r - 1, c, grid);
                add_queue(r, c + 1, grid);
                add_queue(r, c - 1, grid);
            }

            mins++;
        }

        if (fresh == 0) {
            return mins;
        }
        return -1;
    }
};
