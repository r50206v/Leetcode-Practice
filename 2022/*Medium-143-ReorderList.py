from collections import deque

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        q = deque()
        nxt = head.next
        
        # 建立所有node 的queue
        while nxt:
            q.append(nxt)
            nxt = nxt.next
        
        # 0th pos
        prev = head
        # nth pos
        nxt = q.pop()
        i = 0
        while nxt:
            # 0 -> n
            prev.next = nxt
            # 現在prev = nth pos
            prev = nxt
            if len(q) == 0:
                nxt.next = None
                break
            
            # pop -> 1th
            # popleft -> n-1 th
            nxt = q.pop() if i % 2 else q.popleft()
            i += 1
        return