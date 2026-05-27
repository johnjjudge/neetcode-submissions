class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            val = operations[i]
            if val == "+":
                stack.append(stack[-1]+stack[-2])
            elif val == "D":
                stack.append(stack[-1]*2)
            elif val == "C":
                stack.pop()
            else:
                stack.append(int(val))
        return sum(stack)
