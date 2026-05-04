# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
        
        previous = slow
        next_pointer = previous.next

        while next_pointer:
            temp_pointer = next_pointer.next
            next_pointer.next = previous
            previous = next_pointer
            next_pointer = temp_pointer

        left = head
        right = fast

        while left!=slow and right!=slow:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
        
        slow.next = None
              