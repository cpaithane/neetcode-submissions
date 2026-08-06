class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suff = [0] * len(height)

        i = 0
        max_so_far = height[0]
        for h in height:
            max_so_far = max(h, max_so_far)
            pre[i] = max_so_far
            i += 1

        i = len(height) - 1
        max_so_far = height[i]
        while i >= 0:
            h = height[i]
            max_so_far = max(h, max_so_far)
            suff[i] = max_so_far
            i -= 1

        i = 0
        area = 0
        while i < len(height):
            area += min(pre[i], suff[i]) - height[i]
            i += 1

        return area