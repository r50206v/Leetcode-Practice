'''
using recursion dfs to trim the binary tree
and using the characteristic that binary tree 
has smaller element on the left side and 
larger element on the right side 

time: O(N)
space: O(N), the call stack of our recursion could be as large
as the number of nodes in the worst case.
'''
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        def trim(tree):
            if not tree:
                return None
            elif tree.val > high:
                return trim(tree.left)
            elif tree.val < low:
                return trim(tree.right)
            else:
                tree.left = trim(tree.left)
                tree.right = trim(tree.right)
                return tree
            
        return trim(root)