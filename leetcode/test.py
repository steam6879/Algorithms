class Solution(object):
    def swapPairs(self, curr):
        if not curr or not curr.next: return curr
        dummy = ListNode(0)
        dummy.next = curr
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next       
    
# Iteratively
def swapPairs1(self, curr):
    dummy = p = ListNode(0)
    dummy.next = curr
    while curr and curr.next:
        tmp = curr.next
        curr.next = tmp.next
        tmp.next = curr
        p.next = tmp
        curr = curr.next
        p = tmp.next
    return dummy.next