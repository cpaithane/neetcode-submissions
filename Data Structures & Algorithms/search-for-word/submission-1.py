class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        # If word is empty.
        if len(word) == 0:
            return True

        # No need to pass the res string as we are adding
        # chars which are matching with the word
        def backtrack(r, c, idx):
            # Base conditions
            if idx == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                idx > len(word) or
                word[idx] != board[r][c]):
                return False

            visited.add((r, c))

            rc = (backtrack(r + 1, c, idx + 1) or
                 backtrack(r - 1, c, idx + 1) or
                 backtrack(r, c + 1, idx + 1) or
                 backtrack(r, c - 1, idx + 1))

            visited.remove((r, c))
            return rc

        for r in range(0, rows):
            for c in range(0, cols):
                found = backtrack(r, c, 0)
                if found == True:
                    return True
        
        return False