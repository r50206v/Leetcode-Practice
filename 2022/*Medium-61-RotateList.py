class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr = head
        queue = []
        while curr:
            queue.append(curr)
            curr = curr.next
            
        length = len(queue)
        k = k % length
        if k == 0:
            return head
        start = queue[-k]
        end = queue[-(k+1)]
        end.next = None
        
        curr = start
        while curr.next:
            curr = curr.next
        curr.next = head
        
        return start