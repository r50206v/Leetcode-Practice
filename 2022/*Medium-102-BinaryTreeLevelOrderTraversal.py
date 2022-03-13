'''
dfs
time: O(N)
space: O(N)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        def dfs(root, level=0):
            if not root:
                return 
            
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            
            dfs(root.left, level=level + 1)
            dfs(root.right, level=level + 1)
            return ans
        
        return dfs(root)