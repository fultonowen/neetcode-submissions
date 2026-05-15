class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arithmetic = [ '+', '-', '*', '/']
        stack = []
        for item in tokens:
            if not stack:
                stack.append(int(item))
                continue
            if stack and item in arithmetic:
                right, left = stack.pop(), stack.pop()
                
                if item == '+':
                    stack.append(left + right)
                elif item == '-':
                    stack.append(left - right)
                elif item == '*':
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
            else:
                stack.append(int(item))
            print(stack)

        return stack[-1]