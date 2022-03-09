'''
loop over all nodes
time: O(N)
space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0, head)

        prev = result
        
        while head:
            
            if head.next and head.val == head.next.val:
                
                while head.next and head.val == head.next.val:
                    head = head.next
                
                prev.next = head.next
                
            else:
                prev = prev.next
                
            head = head.next
        
        return result.next