# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        p = dummy
        offset = 0 
        while l1 and l2:
            tempSum = l1.val + l2.val + offset
            offset = tempSum // 10
            q = ListNode(tempSum%10, None)
            p.next = q
            p = q
            l1 = l1.next
            l2 = l2.next

        if l1:
            p.next = l1
            previous = None
            while l1 and offset > 0:
                tempSum = l1.val + offset
                l1.val = tempSum%10
                offset = tempSum // 10
                previous = l1
                l1 = l1.next
            if offset > 0:
                previous.next = ListNode(offset, None)
        elif l2:
            p.next = l2
            previous = None
            while l2 and offset > 0:
                tempSum = l2.val + offset
                l2.val = tempSum%10
                offset = tempSum // 10
                previous = l2
                l2 = l2.next
            if offset > 0:
                previous.next = ListNode(offset, None)
        else:
            if offset > 0:
                p.next = ListNode(offset, None)
        
        return dummy.next


