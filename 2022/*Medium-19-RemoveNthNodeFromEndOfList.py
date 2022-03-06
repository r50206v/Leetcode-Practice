'''
two pass
time: O(N)
space: O(N)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = head
        rn = head

        #We start counting the nodes.
        nodes = 1
        while length.next != None:
            nodes += 1
            length = length.next

       #Let's say that nodes are 1=> 2=> 3, and n = 3. 
       #We would remove the first node. So we just simply return rn.next, without going for the second iteration.
        if nodes == n:
            return rn.next

        times = nodes - n -1
        #Second iteration
        for i in range(times):
            head = head.next

        head.next = head.next.next
        return rn



'''
one pass
time: O(N)
space: O(N)
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        nth = None # node to remove
        nth_prev = None # before node to remove
        nth_next = head # after node to remove
        
        counter = 0
        while cur:
            counter += 1
            if counter >= n:
                nth_prev = nth
                nth = nth_next
                nth_next = nth_next.next
            cur = cur.next
        
        if not nth_prev:
            return nth_next # removing head
        else:
            nth_prev.next = nth_next # remove nth
            return head