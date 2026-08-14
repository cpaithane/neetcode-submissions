class Solution {
public:
    bool is_valid_row(vector<vector<char>>& board) {
        for (int i = 0; i < board.size(); i++) {
            unordered_set<char> hash;

            for (int j = 0; j < board[i].size(); j++) {
                if (board[i][j] == '.') {
                    continue;
                }

                if (hash.find(board[i][j]) != hash.end()) {
                    return false;
                }
                hash.insert(board[i][j]);
            }
        }
        return true;
    }

    bool is_valid_col(vector<vector<char>>& board) {
        for (int j = 0; j < 9; j++) {
            unordered_set<char> hash;

            for (int i = 0; i < 9; i++) {
                if (board[i][j] == '.') {
                    continue;
                }

                if (hash.find(board[i][j]) != hash.end()) {
                    return false;
                }
                hash.insert(board[i][j]);
            }
        }
        return true;
    }

    bool is_valid_grid(vector<vector<char>>& board) {
        for (int g = 0; g < 9; g++) {
            unordered_set<char> hash;
    
            for (int i = 0; i < 3; i++) {

                for (int j = 0; j < 3; j++) {
                    int r = (g / 3) * 3 + i;
                    int c = (g % 3) * 3 + j;
                    
                    if (board[r][c] == '.') {
                        continue;
                    }

                    if (hash.find(board[r][c]) != hash.end()) {
                        return false;
                    }
                    hash.insert(board[r][c]);
                }
            }
        }
        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        bool is_valid = is_valid_row(board);
        if (is_valid == false) {
            return false;
        }

        is_valid = is_valid_col(board);
        if (is_valid == false) {
            return false;
        }

        is_valid = is_valid_grid(board);
        if (is_valid == false) {
            return false;
        }
        return true;
    }
};
