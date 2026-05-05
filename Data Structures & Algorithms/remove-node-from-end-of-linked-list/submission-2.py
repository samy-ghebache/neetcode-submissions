class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)   # node fantôme devant head
        fast = slow = dummy
        
        # 1. Avance fast de n pas
        for _ in range(n):
            fast = fast.next
        
        # 2. Avance les deux ensemble jusqu'à ce que fast soit sur le dernier node
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 3. slow est juste AVANT le node à supprimer → bypass
        slow.next = slow.next.next
        
        return dummy.next