class Solution {
private:
    int inf, rows, cols;
    queue<pair<int, int>> q;
    set<pair<int, int>> visited;

    void add_queue(int r, int c, vector<vector<int>>& grid) {
        if (r < 0 ||
            r >= rows ||
            c < 0 ||
            c >= cols ||
            visited.find({r, c}) != visited.end() ||
            grid[r][c] == -1) {
            return;
        }

        q.push({r, c});
        visited.insert({r, c});
    }

public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int dist = 0;
        int level_size = 0;
        inf = 2147483647;
        rows = grid.size();
        cols = grid[0].size();

        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c] == 0) {
                    add_queue(r, c, grid);
                }
            }
        }

        while (!q.empty()) {
            level_size = q.size();
            for (int i = 0; i < level_size; i++) {
                auto [r, c] = q.front();
                q.pop();
                grid[r][c] = dist;

                add_queue(r + 1, c, grid);
                add_queue(r - 1, c, grid);
                add_queue(r, c + 1, grid);
                add_queue(r, c - 1, grid);
            }

            dist++;
        }
    }
};
