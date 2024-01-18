from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        head = mergedList

        while list1 and list2:
            if list1.val > list2.val:
                mergedList.next = ListNode(list2.val)
                list2 = list2.next
            else:
                mergedList.next = ListNode(list1.val)
                list1 = list1.next

            mergedList = mergedList.next

        # Append the remaining elements from list1 or list2
        if list1:
            mergedList.next = list1
        elif list2:
            mergedList.next = list2

        return head.next  # Return the actual head of the merged list
