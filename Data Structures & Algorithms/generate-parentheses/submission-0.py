class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def generateCore(o: int, c: int) -> bool:
            print(o, c, n)
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
        print(res)
        return res
