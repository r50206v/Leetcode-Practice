'''
time: O(N)
space: O(N)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        
        while head:
            
            print(curr.val, head.val)
            if head:
                head = head.next
                count += 1
                
                if count % 2 == 0:
                    curr = curr.next
        return curr