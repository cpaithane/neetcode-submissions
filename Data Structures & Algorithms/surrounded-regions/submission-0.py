class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Let's think in reverse for this.
        # If border has O then the region is not surrounded by x
        # In this case, we need to scan border rows and cols and issue
        # dfs only if there is o. dfs should be 4 directional.
        # As we are issuing dfs on border elements having O, we need to
        # mark them as unsurrounded region by converting it to T
        # By this way, we will have 3 conditions:
        # 1. X -> No change.
        # 2. O -> Is having surrounded region by X. Convert this to X
        # 3. T -> Unsurrounded region. Convert it back to O

        rows = len(board)
        cols = len(board[0])

        def capture(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"):
                return

            print(r, c)
            board[r][c] = "T"

            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)

        for r in range(0, rows):
            if board[r][0] == "O":
                capture(r, 0)
            
        for c in range(0, cols):
            if board[0][c] == "O":
                capture(0, c)

        for r in range(0, rows):
            if board[r][cols - 1] == "O":
                capture(r, cols - 1)

        for c in range(0, cols):
            if board[rows - 1][c]:
                capture(rows - 1, c)

        for r in range(0, rows):
            for c in range(0, cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
