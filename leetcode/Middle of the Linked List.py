from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        count = 0
        while curr.next:
            count += 1
            curr = curr.next
        
        mid = count // 2

        for _ in range(mid):
            head = head.next
        
        return head

class Solution(object):
    def middleNode(self, head):
        # While slow moves one step forward, fast moves two steps forward.
        # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow