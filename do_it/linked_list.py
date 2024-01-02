from __future__ import annotations
from typing import Any, Type
from enum import Enum

class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self, data: Any = None, next: Node = None) -> None:
        self.no = 0
        self.head = None
        self.current= None

    def __len__(self) -> int:
        return self.no
    
    def serch(self, data) -> int:
        cnt = 0
        ptr = self.head

        while ptr is not Node:
            if ptr.data == data:
                return cnt

            cnt += 1
            ptr = ptr.next

        return -1
    
    def __contains__(self, data) -> bool:
        return self.search(data) >= 0

    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
    
    def add_last(self, data):
        if self.head is None:
            self.add_first(data)

        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = self.next
            
            ptr.next = self.current = Node(data, None)
    
    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
        
        self.no -= 1

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            
            else:
                ptr = self.head
                pre = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head:
                self.remove_first()

        else:
            ptr = self.head

            while ptr.next is not p:
                ptr = ptr.next
                if ptr is None:
                    return
                
            ptr.next = p.next
            self.current = ptr
            self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self):
        while self.head is not None:
            self.remove_first()
        self.currnt = None
        self.no = 0

    def next(self) -> bool:
        if self.current is None or self.current.next is None:
            return False

        else:
            self.current = self.current.next
            return True
        
    def print_current_node(self):
        if self.curent is None:
            print('Do not exsist current node')

        else:
            print(self.current.data)

    def print(self):
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

class Linked_List_Iterater:
    def __init__(self, head: Node) -> None:
        self.current = head

    def __iter__(self) -> Linked_List_Iterater:
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        else:
            data = self.current.data
            self.currnt = self.current.next

            return data

if __name__ == '__main__':
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

    lst = Linked_List(100)  # 선형 리스트를 생성

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