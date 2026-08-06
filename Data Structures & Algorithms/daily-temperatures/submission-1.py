class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # For every current element, compare with top of stack.
        # Till cur > top, then pop and fill the res
        # Else push to stack.
        for i, cur in enumerate(temperatures):
            while stack and cur > stack[-1][0]:
                top, top_idx = stack.pop()
                res[top_idx] = i - top_idx
            stack.append((cur, i))

        return res