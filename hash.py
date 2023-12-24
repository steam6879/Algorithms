from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

#chainning
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

#open addressing
class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    def __init__(self, key, value, stat) -> None:
        self.key = key  #key
        self.value = value  #value
        self.stat = stat    #status(속성)
    
    def set(self, key, value, stat) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        self.stat = stat

# class OpenHash:
#     def __init__(self, capacity) -> None:
#         self.capacity = capacity
#         self.table = [Bucket()] * self.capacity  #hash table

class OpenHash:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.table = [Bucket(None, None, Status.EMPTY) for _ in range(self.capacity)]

    def hash_value(self, key) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def rehash_value(self, key) -> int:
        return (self.hash_value(key) + 1) % self.capacity
    
    def search_node(self, key) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            
            hash = self.rehash_value(hash)
            p = self.table[hash]

        return None
    
    def search(self, key) -> Any:
        p = self.search_node(key)
        
        if p is not None:
            return p.value
        
        else:
            return None
        
    def add(self, key, value) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        return False    #hash table is full
    
    def remove(self, key) -> int:
        p = self.search_node(key)
        
        if p is None:
            return False
        
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            
            elif self.table[i].stat == Status.EMPTY:
                print('-- unregistered --')
            
            elif self.table[i].stat == Status.DELETED:
                print('-- deleted --')


#main
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

# hash = ChainedHash(13)
hash = OpenHash(13)

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