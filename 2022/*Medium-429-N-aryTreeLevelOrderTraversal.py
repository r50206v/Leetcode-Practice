"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = [(root, 0)]
        
        while queue:
            
            node, idx = queue.pop(0)
            if len(ans) <= idx:
                ans.append([node.val])
            else:
                ans[idx].append(node.val)
                
            for next_node in node.children:
                queue.append((next_node, idx+1))
        return ans