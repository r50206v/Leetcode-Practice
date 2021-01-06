# 21. Merge Two Sorted Linked Lists
'''
iteration: 
time: O(n + m)
space: O(1)
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        head = ListNode()
        tmp = head
        while l1 or l2:
            if not l1 and l2:
                tmp.val = l2.val
                tmp.next = l2.next
                break
            elif l1 and not l2:
                tmp.val = l1.val
                tmp.next = l1.next
                break
            
            if l1.val < l2.val:
                tmp.val = l1.val
                l1 = l1.next
            else:
                tmp.val = l2.val
                l2 = l2.next
            
            tmp.next = ListNode()
            tmp = tmp.next
        return head

'''
recursion
time: O(n + m)
space: O(n + m) n+m stacks for recursions
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2