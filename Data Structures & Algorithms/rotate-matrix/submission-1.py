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
            # Rotation will happen in corners of the square.
            for i in range(right - left):
                print(left, right)
                top = left
                bottom = right
                top_left = matrix[top][left + i]
                
                # top-left - Bottom Left. Column is incrementing for top-left
                # Row is decrementing for bottom-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Bottom-left - Bottom Right. Column is decrementing for bottom right.
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Bottom Right - Top Right. Row is incrementing for top right.
                matrix[bottom][right - i] = matrix[top + i][right]

                # Top Right - Top Left. Assign top_left to the top right.
                matrix[top + i][right] = top_left

            left += 1
            right -= 1