from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = {}
        while head:
            if head in m:
                return True
            else:
                m[head] = True

            head = head.next

        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m = set()

        while head:
            if head in m:
                return True
            else:
                m.add(head)
                head = head.next

        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
