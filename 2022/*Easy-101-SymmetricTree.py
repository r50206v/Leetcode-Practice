# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        if not root.left and not root.right:
            return root
        
        def left_dfs(root):
            if not root:
                return [None]
            left.append(root.val)
            left.append(left_dfs(root.left))
            left.append(left_dfs(root.right))
                
        def right_dfs(root):
            if not root:
                return [None]
            right.append(root.val)
            right.append(right_dfs(root.right))
            right.append(right_dfs(root.left))
                
        left = []
        left_dfs(root)
        right = []
        right_dfs(root)
        
        print(left, right)
        return left == right



'''
public boolean isSymmetric(TreeNode root) {
    return isMirror(root, root);
}

public boolean isMirror(TreeNode t1, TreeNode t2) {
    if (t1 == null && t2 == null) return true;
    if (t1 == null || t2 == null) return false;
    return (t1.val == t2.val)
        && isMirror(t1.right, t2.left)
        && isMirror(t1.left, t2.right);
}
'''