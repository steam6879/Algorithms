from typing import Any
from enum import Enum

class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, x) -> None:
        if self.is_full():
            raise FixedQueue.Full
        
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1    # increment no of elements in queue
        
        if self.rear == self.capacity:
            self.rear = 0   # reset rear to 0 when it reaches the end of the queue

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        
        x = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0

        return x
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        
        return self.que[self.front]
    
    def find(self, value) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
        
            if self.que[idx] == value:
                return idx
            
        return -1
    
    def count(self, value) -> bool:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity

            if self.que[idx] == value:
                c += 1
            
        return c
        
    def __contains__(self, value) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('Queue is empty')

        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = ' ')
            
            print()

#fixed queue test

Menu = Enum('Menu', ['Enque', 'Deque', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    
    while True:
        print(*s, sep= ' ', end = '')
        n = int(input(': '))

        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'current data: {len(q)} / {q.capacity}')
    menu = select_menu()

    if menu == Menu.Enque:
        x = int(input('data: '))

        try:
            q.enque(x)
        
        except FixedQueue.Full:
            print('Queue is full')

    elif menu == Menu.Deque:
        try:
            x = q.deque()
            print(f'dequeued data is {x}')

        except FixedQueue.Empty:
            print('Queue is empty')

    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'peeked data is {x}')

        except FixedQueue.Empty:
            print('Queue is empty')

    elif menu == Menu.Search:
        x = int(input('value: '))

        if x in q:
            print(f'{q.count(x)} times, the value {x} is at {q.find(x)}')

        else:
            print('No such value')

    elif menu == Menu.Dump:
        q.dump()

    else:
        break
    