# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        result = ListNode(val=head.val)
        while head.next:
            
            head = head.next
            result = ListNode(head.val, result)
        
        return result