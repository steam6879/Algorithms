from __future__ import annotations
from typing import Any, Type
from enum import Enum

class Node:
    def __init__(self, data = None, prev = None, next = None) -> None:
        self.data = data
        self.prev = prev or self
        self.next = next or self

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.no = 0

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.head.next is self.head
    
    def search(self, data) -> Any:
        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                return cnt
            
            cnt += 1
            ptr = ptr.next
        
        return -1

    def __contains__(self, data) -> bool:
        return self.search(data) >= 0
    
    def print_current_node(self) -> None:
        if self.is_empty():
            print('There is no current node.')
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head.next
        
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        ptr = self.head.prev

        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        if self.is_empty() or self.current.next is self.head:
            return False
        
        self.current = self.current.next

        return True
    
    def prev(self) -> bool:
        if self.is_empty() or self.current.prev is self.head:
            return False
        
        self.current = self.current.prev

        return True
    
    def add(self, data) -> None:
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data) -> None:
        self.current = self.head
        self.add(data)

    def add_last(self, data) -> None:
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1

            if self.current is self.head:
                self.current = self.head.next
        
    def remove(self, p: Node) -> None:
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break

            ptr = ptr.next

    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()

    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()

    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()

    def __iter__(self) -> DoubleLinkedListIterator:
        return DoubleLinkedListIterator(self, self.head)
    
    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        return DoubleLinkedListReverseIterator(self, self.head)
    
class DoubleLinkedListIterator:
    def __init__(self, lst: DoubleLinkedList, head: Node) -> None:
        self.lst = lst
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            
            raise StopIteration
        
        else:
            data = self.current.data
            self.current = self.current.next

            return data
        
class DoubleLinkedListReverseIterator:
    def __init__(self, lst: DoubleLinkedList, head: Node) -> None:
        self.lst = lst
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current is self.head:
            
            raise StopIteration
        
        else:
            data = self.current.data
            self.current = self.current.prev

            return data
        

Menu = Enum('Menu', ['insert_node_at_head', 'insert_node_at_tail', 'insert_node_after_current',
                     'delete_head_node', 'delete_tail_node', 'print_current_node',
                     'move_to_next_node', 'move_to_previous_node', 'delete_current_node',
                     'delete_all_nodes', 'search', 'membership_check', 'print_all_nodes',
                     'print_all_nodes_in_reverse', 'scan_all_nodes', 'scan_all_nodes_in_reverse', 'exit'])

def select_menu() -> Menu:
    """Menu selection"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        print()
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()  # Create a circular double linked list

while True:
    menu = select_menu()  # Select menu

    if menu == Menu.insert_node_at_head:  # Insert node at the head
        lst.add_first(int(input('Enter the value to insert at the head node: ')))

    elif menu == Menu.insert_node_at_tail:  # Insert node at the tail
        lst.add_last(int(input('Enter the value to insert at the tail node: ')))

    elif menu == Menu.insert_node_after_current:  # Insert node after the current node
        lst.add(int(input('Enter the value to insert after the current node: ')))

    elif menu == Menu.delete_head_node:  # Delete the head node
        lst.remove_first()

    elif menu == Menu.delete_tail_node:  # Delete the tail node
        lst.remove_last()

    elif menu == Menu.print_current_node:  # Print the current node
        lst.print_current_node()

    elif menu == Menu.move_to_next_node:  # Move to the next node
        lst.next()

    elif menu == Menu.move_to_previous_node:  # Move to the previous node
        lst.prev()

    elif menu == Menu.delete_current_node:  # Delete the current node
        lst.remove_current_node()

    elif menu == Menu.delete_all_nodes:  # Delete all nodes
        lst.clear()

    elif menu == Menu.search:  # Search
        pos = lst.search(int(input('Enter the value to search: ')))
        if pos >= 0:
            print(f'The data is at the {pos + 1}th position.')
        else:
            print('The data does not exist.')

    elif menu == Menu.membership_check:  # Membership check
        print('The data is included'
              +('.' if int(input('Enter the value to check: ')) in lst else ' not.'))

    elif menu == Menu.print_all_nodes:  # Print all nodes
        lst.print()

    elif menu == Menu.print_all_nodes_in_reverse:  # Print all nodes in reverse
        lst.print_reverse()

    elif menu == Menu.scan_all_nodes:  # Scan all nodes
        for e in lst:
             print(e)

    elif menu == Menu.scan_all_nodes_in_reverse:  # Scan all nodes in reverse
        for e in reversed(lst):
             print(e)

    else:  # Exit
        break