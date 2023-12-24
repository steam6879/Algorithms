from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity # 해시 테이블(리스트)을 선언

    def hash_value(self, key):
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) # return hash(key) % self.capacity
    
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

    def add(self, key, value):
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key):
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = pp = p.next
            return False

    def dump(self):
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()


from enum import Enum

Menu = Enum('Menu', ['Add', 'Delete', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')       
        #The reason for using *s instead of s is to unpack the iterable (like a list or tuple) in Python.
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
            #Menu(n) serves to convert the user's choice into a Menu enum value.

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.Add:
        key = int(input('Enter the key: '))
        val = input('Enter the value: ')
        if not hash.add(key, val):
            print('Failed to add the data')

    elif menu == Menu.Delete:
        key = int(input('Enter the key: '))
        if not hash.remove(key):
            print('Failed to delete the data')

    elif menu == Menu.Search:
        key = int(input('Enter the key: '))
        t = hash.search(key)
        if t is not None:
            print(f'The value is {t}')
        else:
            print('No data')

    elif menu == Menu.Dump:
        hash.dump()

    else:
        break