# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = prev = ListNode(0)
        dummy.next = curr = head
        
        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = curr
            prev.next = temp

            curr = curr.next
            prev = temp.next

        return dummy.next
    
