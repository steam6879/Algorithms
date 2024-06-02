# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        count = 0

        while head:
            count += 1
            head = head.next

        targetIndex = count - n

        if targetIndex == 0:
            return dummy.next.next

        for _ in range(targetIndex - 1):
            curr = curr.next
            curr.next = curr.next.next

        return dummy.next