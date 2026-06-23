class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left+right)
            elif tokens[i] == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left-right)
            elif tokens[i] == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left*right)
            elif tokens[i] == '/':
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left/right))
            else:
                stack.append(int(tokens[i]))
            i += 1
        return int(stack.pop())