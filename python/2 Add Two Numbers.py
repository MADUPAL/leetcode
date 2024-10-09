# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            cur.next = ListNode(l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        cur.next = l1 or l2

        cur = dummy.next
        prev = dummy
        n = 0
        while cur:
            if n > 0:
                cur.val += n
            n = cur.val // 10
            cur.val %= 10
            cur = cur.next
            prev = prev.next
        if n > 0:
            prev.next = ListNode(n)

        # cur = dummy.next
        # while cur:
        #     print(cur.val)
        #     cur = cur.next
        
        return dummy.next