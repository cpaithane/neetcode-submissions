class Solution:
    def can_attack(self, row, rows, col, cols, board):
        # Check cols
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return True

            r -= 1
    
        # Left upper diagonal
        r = row - 1
        c = col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return True

            r -= 1
            c -= 1

        # Upper right diagonal
        r = row - 1
        c = col + 1
        while r >= 0 and c < cols:
            if board[r][c] == "Q":
                return True

            r -= 1
            c += 1

        # No need to check row -> n, col -> n as they are not filled up yet
        return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        res_list = []
        #board = [["."]*n]*n
        #board = [["."] * n for i in range(n)]

        board = []
        for r in range(0, n):
            row = ["."] * n
            board.append(row)

        print(board)

        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res_list.append(copy)
                return

            for c in range(0, n):
                if self.can_attack(r, n, c, n, board) == False:
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."

        backtrack(0)
        return res_list