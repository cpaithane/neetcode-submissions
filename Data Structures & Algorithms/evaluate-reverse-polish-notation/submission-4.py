class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                res = None

                if token == "+":
                    res = (num1 + num2)
                elif token == "-":
                    res = (num1 - num2)
                elif token == "*":
                    res = (num1 * num2)
                elif token == "/":
                    res = int(num1 / num2)
                
                stack.append(res)
            else:
                stack.append(int(token))
        
        return (stack[0])
