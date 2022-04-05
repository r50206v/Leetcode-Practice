'''
hashmap
time: O(N + M)
space: O(N)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if not headA or not headB:
            return None
        
        setA = set([])
        currA = headA
        while currA: 
            setA.add(currA)
            currA = currA.next
            
        currB = headB
        while currB:
            if currB in setA:
                return currB
            
            currB = currB.next
        
        return None

'''
two pointers
time: O(N + M)
space: O(1)
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA
        # Note: In the case lists do not intersect, the pointers for A and B
        # will still line up in the 2nd iteration, just that here won't be
        # a common node down the list and both will reach their respective ends
        # at the same time. So pA will be NULL in that case.