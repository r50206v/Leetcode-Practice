'''
My solution:
DFS + stack

time: O(N)
space: O(N)
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head:
            return None 
        
        prev = None
        nodeStack = [head]
        
        while nodeStack:
            curr = nodeStack.pop()
            
            if prev:
                prev.next = curr
            curr.prev = prev
            
            if curr.next:
                nodeStack.append(curr.next)
            
            if curr.child:
                nodeStack.append(curr.child)
                curr.child = None
            prev = curr
            
        return head