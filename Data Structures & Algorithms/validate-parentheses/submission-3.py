class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBrackets = ['(', '{', '[']
        closedBrackets = [')', '}', ']']
        length = len(s)
        if length%2 == 1:
            return False
        else:
            for i in s:
                if i in openBrackets:
                    stack.append(i)
                elif i in closedBrackets:
                    if len(stack) == 0:
                        return False
                    elif i == ')' and stack[-1] != '(':
                        return False
                    elif i == '}' and stack[-1] != '{':
                        return False
                    elif i == ']' and stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
            if len(stack) != 0:
                return False
            else:
                return True
