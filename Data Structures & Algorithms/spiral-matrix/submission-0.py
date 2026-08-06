class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # top and left starts from 0
        # bottom is no. of rows, right is no. of cols.
        top = 0
        bottom = len(matrix)
        
        left = 0
        right = len(matrix[0])
        res_list = []

        while left < right and top < bottom:
            # Go from left -> right, col will change
            for i in range(left, right):
                res_list.append(matrix[top][i])

            top += 1

            # Go from top -> bottom, row will change
            for i in range(top, bottom):
                res_list.append(matrix[i][right - 1])
            
            right -= 1

            if not (left < right and top < bottom):
                break

            # Go from right -> left, col will change
            for i in range(right - 1, left - 1, -1):
                res_list.append(matrix[bottom - 1][i])

            bottom -= 1

            # Go from bottom -> top, row will change
            for i in range(bottom - 1, top - 1, -1):
                res_list.append(matrix[i][left])

            left += 1

        return res_list