from typing import Any
from enum import Enum

class FixedStack:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0 
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        
        return self.stk[self.ptr - 1]
    
    def clear(self):
        self.ptr = 0

    def find(self, value) -> Any:
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
            
        return -1
    
    def count(self, value) -> bool:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1

        return c
    
    def __contains__(self, value) -> bool:
        return self.count(value) > 0
    
    def dump(self) -> None:
        if self.is_empty():
            print('Stack is empty')

        else:
            print(self.stk[:self.ptr])

#FixedStack test
Menu = Enum('Menu', ['Push', 'Pop', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]

    while True:
        print(*s, sep = ' ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
        
#main
s = FixedStack((64)
               
while True:
    print(f'current data: {len(s)} / {s.capacity}')
    menu = select_menu()

    if menu == Menu.Push:
        x = int(input('data: '))
        try:
            s.Push(x)
        except FixedStack.Full:
            print('Stack is full')

    elif menu == Menu.Pop:
        