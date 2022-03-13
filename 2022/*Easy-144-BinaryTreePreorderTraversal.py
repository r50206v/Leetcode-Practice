# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root):
            
            if not root:
                return []
            
            ans = [root.val]
            if root.left:
                ans = ans + dfs(root.left)
            
            if root.right:
                ans = ans + dfs(root.right)
                
            return ans
    
        return dfs(root)