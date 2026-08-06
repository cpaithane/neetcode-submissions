class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, cur in enumerate(temperatures):
            while stack and cur > stack[-1][0]:
                top, top_idx = stack.pop()
                res[top_idx] = i - top_idx
            stack.append((cur, i))

        return res