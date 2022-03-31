# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 or not l2:
            return l1 or l2
        
        stack1 = []
        stack2 = []
        l1_head = l1
        l2_head = l2
        while l1_head or l2_head:
            if l1_head:
                stack1.append(l1_head)
                l1_head = l1_head.next
            if l2_head:
                stack2.append(l2_head)
                l2_head = l2_head.next
        
        if len(stack2) > len(stack1):
            stack1, stack2 = stack2, stack1
        
        carry = 0
        while stack1:
            node1 = stack1.pop(-1)
            carry += node1.val
            
            if stack2:
                node2 = stack2.pop(-1)
                carry += node2.val
            
            node1.val = carry % 10
            carry = carry // 10
            
            
        if carry and stack1:
            node1 = stack1.pop(-1)
            node1.val += 1
        elif carry:
            node = ListNode(1)
            node.next = node1
            node1 = node
        
        return node1