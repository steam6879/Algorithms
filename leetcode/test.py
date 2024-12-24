class MyQueue:

    def __init__(self):
        self.que = collections.deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.que:
            return self.que.popleft()

    def peek(self) -> int:
        if self.que:
            return self.que[0]

    def empty(self) -> bool:
        return not self.que


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()