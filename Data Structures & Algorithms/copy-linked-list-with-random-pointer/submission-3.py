class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Pass 1: interweave copies into the original list
        # A -> B -> C   becomes   A -> A' -> B -> B' -> C -> C'
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next   # skip over the copy we just inserted

        # Pass 2: assign random pointers to the copies
        # A'.random is the node right after A.random (which is the copy of A.random)
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next   # skip original AND its copy

        # Pass 3: detach the copy list from the original
        # Restore A -> B -> C and extract A' -> B' -> C'
        cur = head
        copy_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next                          # restore original
            copy.next = copy.next.next if copy.next else None  # advance copy chain
            cur = cur.next

        return copy_head