'''
Runtime: 96 ms
Memory Usage: 13.8 MB
'''
# Recursive
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
    
    
    
# Loop
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # If either is not present, return the other
    if not (l1 or l2):
        return l1 or l2

    node = head = ListNode(None)        
    carry = 0

    while l1 or l2 or carry:
        summary = carry
        if l1:
            summary += l1.val
            l1 = l1.next
        if l2:
            summary += l2.val
            l2 = l2.next
        
        carry = summary // 10
        summary = summary % 10
        node.next = ListNode(summary)
        node = node.next

    return head.next