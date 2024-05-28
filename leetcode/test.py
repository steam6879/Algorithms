from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        
        count = 0
        
        while head:
            head = head.next
            count += 1

        for _ in range(count // 2):
            temp = temp.next

        return temp