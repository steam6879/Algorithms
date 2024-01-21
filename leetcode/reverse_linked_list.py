from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None, ):
        self.val = val
        self.next = next

#recursive algoritm
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        newTail = head.next
        newHead = self.reverseList(head.next)

        newTail.next = head
        head.next = None

        return newHead

#iteratively algorithm
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, curr = None, head
#         node = head
#         while curr:
#             tempNext = curr
#             curr.next = prev
#             prev, curr = curr, tempNext.next
        
#         return prev

#stack algorithm
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         stack = []
#         node = head

#         while node:
#             stack.append(node)
#             node = node.next
        
#         dummy = ListNode(-1)
#         node = dummy

#         while stack:
#             node.next = stack.pop
#             node = node.next
        
#         node.next = None

#         return dummy.next

#https://www.youtube.com/watch?v=O4po8XPf5Hc&t=2s