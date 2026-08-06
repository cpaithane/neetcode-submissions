class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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
        