class Solution {
private:
    set<pair<int, int>> visited;

public:
    bool backtrack(int r, int c, int i, vector<vector<char>>& board, string &word) {
        if (word.size() == i) {
            return true;
        }

        if (r < 0 || r >= board.size() ||
            c < 0 || c >= board[0].size() ||
            visited.find({r, c}) != visited.end() ||
            i > word.size() ||
            board[r][c] != word[i]) {
                return false;
        }

        visited.insert({r, c});
        bool found = backtrack(r + 1, c, i + 1, board, word) ||
                     backtrack(r, c + 1, i + 1, board, word) ||
                     backtrack(r - 1, c, i + 1, board, word) ||
                     backtrack(r, c - 1, i + 1, board, word);

        visited.erase({r, c});
        return found;
    } 

    bool exist(vector<vector<char>>& board, string word) {
        if (word.size() == 0) {
            return true;
        }

        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (backtrack(r, c, 0, board, word) == true) {
                    return true;
                }
            }
        }

        return false;
    }
};
