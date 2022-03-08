# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        result = ListNode(0)
        result.next = head
        
        prev, curr = result, head
        while curr:
            if curr.val != val:
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        
        return result.next