class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        # Use backtracking here. Push ( on stack till n
        # Push ) on stack till c becomes 0.
        # When c and 0 both becomes n, append the result in stack.
        # And pop from stack.
        def generateCore(o: int, c: int) -> bool:
            if c == n and o == n:
                res.append("".join(stack))
                return

            if o < n:
                stack.append("(")
                generateCore(o+1, c)
                stack.pop()
        
            if c < o:
                stack.append(")")
                generateCore(o, c+1)
                stack.pop()

        generateCore(0, 0)
        return res
