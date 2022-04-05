'''
hashmap
time: O(N)
space: O(N)
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: 
            return None
        
        seen = set([])
        curr = head
        
        while curr: 
            if curr in seen:
                return curr
            else:
                seen.add(curr)
            
            curr = curr.next
        
        return None    