# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        reversed_head = head
        previous = None
        
        while reversed_head:
            temp = reversed_head.next
            reversed_head.next = previous
            previous = reversed_head
            reversed_head = temp

        reversed_head = previous
        tempN = n

        previous = reversed_head
        todelete = reversed_head

        while tempN - 1 > 0:
            previous = todelete
            todelete = todelete.next
            tempN -= 1

        if previous == todelete:
            reversed_head = reversed_head.next
        else:
            previous.next = todelete.next

        next_pointer = reversed_head
        previous = None
        while next_pointer:
            temp = next_pointer.next
            next_pointer.next = previous
            previous = next_pointer
            next_pointer = temp
        
        return previous
        