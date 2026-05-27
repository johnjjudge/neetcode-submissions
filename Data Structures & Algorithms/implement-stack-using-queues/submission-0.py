class MyStack:

    def __init__(self):
        self.queue = []
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        for i in range(self.length-1):
            self.queue.append(self.queue[0])
            self.queue.pop(0)
        self.length -= 1
        return self.queue.pop(0)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()