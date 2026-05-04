# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        left = head
        right = head
        stack = []
        while right:
            stack.append(right)
            right = right.next
            
        i = len(stack) - 1
        
        while left != stack[i]:
            left_next = left.next
            right = stack[i]
            if left_next == right:
                right.next = None
                break
            left.next = right
            right.next = left_next
            left = left_next
            i-=1
        
        stack[i].next = None
            
