class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        print(rows, cols)

        for r in range(0, rows):
            # Found the row where the target should present.
            # Now, binary search between this row only.
            if matrix[r][0] <= target and matrix[r][cols-1] >= target:
                row_matr = matrix[r]
                s = 0
                e = cols -1

                while s <= e:
                    mid = (s + ((e-s)//2))
                    if row_matr[mid] == target:
                        return True
                    elif row_matr[mid] < target:
                        s = mid + 1
                    else:
                        e = mid - 1

                # Binary search didn't find the target.
                return False

            elif matrix[r][0] < target:
                r += 1
            else:
                r -= 1

        return False

