# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(None, head)
        prev = result
        
        while head:
            
            if prev.val == head.val:
                prev.next = head.next
                head = head.next
            else:
                head = head.next
                prev = prev.next
                
        return result.next