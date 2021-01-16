'''
time: O(max(M, N))
space: O(max(M, N))
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        
        ans = ListNode()
        ans.val = ((l1.val if l1 else 0) + (l2.val if l2 else 0)) % 10
        
        if ((l1.val if l1 else 0) + (l2.val if l2 else 0)) // 10 > 0:
            
            if l1.next:
                l1.next.val += 1
            else:
                l1.next = ListNode(val=1)
                
        ans.next = self.addTwoNumbers((l1.next if l1 else None), (l2.next if l2 else None))
        return ans