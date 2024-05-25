from typing import Optional, ListNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        dummy = ListNode(-1)
        curr = dummy.next

        
        while list1 and list2:
            if list1.val > list2.val:
                curr = ListNode(list2.val)
                list1 = list1.next
            else:
                curr = ListNode(list1.val)
                list1 = list1.next

            curr =  curr.next
        
        if list1:
            curr = list1
        elif list2:
            curr = list2

        return dummy.next
