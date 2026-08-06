class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1
        max_area = 0

        while s < e:
            area = min(heights[s], heights[e]) * (e - s)
            max_area = max(area, max_area)

            if heights[s] < heights[e]:
                s += 1
            elif heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
                e -= 1

        return max_area