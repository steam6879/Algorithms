from collections import deque


class MyQueue:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.queue:
            return self.queue.popleft()

    def peek(self) -> int:
        if self.queue:
            return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
