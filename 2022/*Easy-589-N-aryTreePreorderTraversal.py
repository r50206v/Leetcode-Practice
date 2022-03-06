"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, output = [root], []
        while stack:
            root = stack.pop(0)
            output.append(root.val)
            if root.children:
                stack = root.children + stack
            
        return output