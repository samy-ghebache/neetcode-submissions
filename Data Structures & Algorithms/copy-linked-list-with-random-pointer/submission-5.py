"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        left = head
        dummy = Node(0)
        previous = dummy
        hashMap = {}
        while left:
            previous.next = Node(left.val)
            previous = previous.next
            hashMap[left] = previous
            left = left.next
            
        left = head
        while left:
            second_node = hashMap[left]
            second_node.random = hashMap.get(left.random)
            left = left.next
        
        return dummy.next
