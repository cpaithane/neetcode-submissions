class Solution {
private:
    int rows, cols;

    void capture(int r, int c, vector<vector<char>>& board) {
        if (r < 0 ||
            r >= rows ||
            c < 0 ||
            c >= cols ||
            board[r][c] != 'O') {
                return;
        }

        board[r][c] = 'T';

        capture(r + 1, c, board);
        capture(r - 1, c, board);
        capture(r, c + 1, board);
        capture(r, c - 1, board);
    }

public:
    void solve(vector<vector<char>>& board) {
        rows = board.size();
        cols = board[0].size();

        for (int r = 0; r < rows; r++) {
            if (board[r][0] == 'O') {
                capture(r, 0, board);
            }
        }

        for (int c = 0; c < cols; c++) {
            if (board[0][c] == 'O') {
                capture(0, c, board);
            }
        }

        for (int r = 0; r < rows; r++) {
            if (board[r][cols - 1] == 'O') {
                capture(r, cols - 1, board);
            }
        }

        for (int c = 0; c < cols; c++) {
            if (board[rows - 1][c] == 'O') {
                capture(rows - 1, c, board);
            }
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X';
                } else if (board[r][c] == 'T') {
                    board[r][c] = 'O';
                }
            }
        }
    }
};
