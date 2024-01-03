from __future__ import annotations
from typing import Any, Type
from enum import Enum

Null = -1

class Node:
    def __init__(self, data = Null, next = Null, dnext = Null) -> None:
        self.data = data
        self.next = next
        self.dnext = dnext

class ArrayLinkedList:
    def __init__(self, capacity) -> None:
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no
    
    def get_insert_index(self):
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            
            else:
                return Null
        
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec
        

    def delete_index(self, idx):
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null

        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec
    
    def search(self, data: Any):
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt

            cnt += 1
            ptr = self.n[ptr].next
        
        return Null
    
    def __contains__(self, data):
        return self.search(data) >= 0  
    
    def add_first(self, data):
        ptr = self.head
        rec = self.get_insert_index()

        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data):
        if self.head == Null:
            self.add_first(data)
        
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            
            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self):
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self):
        if self.head != Null:
            if self.n[self.head].next != Null:
                self.remove_first()
            
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next

                self.n[pre].next = Null
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int):
        if self.head != Null:
            if p == self.pead:
                self.remove_first()
            
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return
                
                self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head != Null:
            self.remove_first()
        self.current = Null

    def next(self):
        if self.current == Null or self.n[self.current].next == Null:
            return False
        
        self.current = self.n[self.current].next
        return True
    
    def print_current_node(self):
        if self.current == Null:
            print('Do not exsist current node')

        else:
            print(self.n[self.current].data)

    def print(self):
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self):
        for i in self.n:
            print(f'[{i}] {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    def __init__(self, n, head) -> None:
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self):
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
        
# [Do it! 실습 8-3] 커서를 이용한 선형 리스트 클래스 ArrayLinkedList 사용하기


Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = ArrayLinkedList(100)  # 선형 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
                                    
    elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:             # 주목 노드를 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:             # 모두 삭제
        lst.clear()

    elif menu == Menu.검색:                     # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:               # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
              +('있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:             # 모든 노드를 출력
        lst.print()

    elif menu == Menu.스캔:                     # 모든 노드 스캔
        for e in lst:
             print(e)

    else:                                       # 종료
        break