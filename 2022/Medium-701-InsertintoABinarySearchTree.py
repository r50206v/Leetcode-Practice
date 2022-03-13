'''
bfs
time: O(H), where H is a tree height. 
    That results in O(logN) in the average case, 
    and O(N) in the worst case.
space: O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        result = root
        queue = [root]
        while queue:
            root = queue.pop(0)
            
            if root.val > val and root.left:
                queue.append(root.left)
            elif root.val < val and root.right:
                queue.append(root.right)
            
            elif root.val > val:
                root.left = TreeNode(val)
            elif root.val < val:
                root.right = TreeNode(val)
        
        return result
                