class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arith = ['*', '-', '+', '/']
        stack = []
        for token in tokens:
            if token in arith:
                right, left = stack.pop(), stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(token))
        return stack[-1]