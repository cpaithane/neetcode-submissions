class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Start from bottom left to top left transition
        # bottom left -> top left
        # bottom right -> bottom left
        # top right -> bottom right
        # top left -> top right

        # Looping part
        # Start from 
        left = 0
        right = len(matrix) - 1

        while left < right:
            for i in range(right - left):
                print(left, right)
                top = left
                bottom = right
                top_left = matrix[top][left + i]
                
                # top-left - Bottom Left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom-left - Bottom Right
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Bottom Right - Top Right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Top Right - Top Left
                matrix[top + i][right] = top_left

            left += 1
            right -= 1