class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Don't zero out first row and col
        rows = len(matrix)
        cols = len(matrix[0])
        rowZero = False

        for r in range(0, rows):
            for c in range(0, cols):
                if matrix[r][c] == 0:
                    # Zero out first element of the col.
                    matrix[0][c] = 0
                    if r == 0:
                        rowZero = True
                    else:
                        # Zero out first element of the row.
                        matrix[r][0] = 0

        # If for any row or col, first element is zero, zero entire row.
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(0, rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(0, cols):
                matrix[0][c] = 0

        return

        r_set = set()
        c_set = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(0, rows):
            for c in range(0, cols):
                if matrix[r][c] == 0:
                    r_set.add(r)
                    c_set.add(c)

        for r in range(0, rows):
            for c in range(0, cols):
                if r in r_set or c in c_set:
                    matrix[r][c] = 0
