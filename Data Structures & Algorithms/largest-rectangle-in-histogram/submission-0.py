class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Store index and height

        for i, h in enumerate(heights):
            t_idx = i
            while stack and stack[-1][1] > h:
                t_idx, t_h = stack.pop()
                maxArea = max(maxArea, t_h * (i - t_idx))

            stack.append((t_idx, h))
        
        # There will be non-empty stack. Calculate maxArea also
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea