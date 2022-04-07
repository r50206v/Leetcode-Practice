'''
iteration 
time: O(N)
space: O(1)
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        idx = 0
        curr = head
        while curr:
            if idx % 2 == 1:
                tmp = curr.next
                prev.val, prev.next.val = curr.val, prev.val
                prev = prev.next
                prev.next = tmp
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
                
            idx += 1
        
        return head

'''
recursion
time: O(N)
space: O(N)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node