class Solution:
    def checkValidRow(self, board: List[List[str]]) -> bool:
        for r in range(0, len(board[0])):
            valid_check = set()
            for c in range(0, len(board[0])):
                if board[r][c] == ".":
                    continue
            
                if board[r][c] in valid_check:
                    return False
            
                valid_check.add(board[r][c])

        return True

    def checkValidCol(self, board: List[List[str]]) -> bool:
        for c in range(0, len(board[0])):
            valid_check = set()
            for r in range(0, len(board[0])):
                if board[r][c] == ".":
                    continue
            
                if board[r][c] in valid_check:
                    return False

                valid_check.add(board[r][c])

        return True

    def isValidGrid(self, board: List[List[str]]) -> bool:
        for g in range(9):
            valid_check = set()
            for i in range(3):
                for j in range(3):
                    # // is for division and rounding down.
                    r = ((g//3)*3 + i);
                    c = ((g%3)*3 + j);

                    if board[r][c] == ".":
                        continue

                    if board[r][c] in valid_check:
                        return False

                    valid_check.add(board[r][c])

        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for duplicates in all rows
        # Check whether numbers 1-9 are present
        valid = self.checkValidRow(board)
        if valid == False:
            return False

        valid = self.checkValidCol(board)
        if valid == False:
            return False

        return self.isValidGrid(board)
