# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root):
            
            if not root:
                return []
            
            ans = []
            if root.left:
                ans = dfs(root.left) + ans
            
            ans.append(root.val)
            
            if root.right:
                ans = ans + dfs(root.right)
                
            return ans
    
        return dfs(root)