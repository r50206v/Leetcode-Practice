'''
dfs
time: O(N)
space: O(N)
'''
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def isConnected(root,head): ##checks if linked list is in the tree
            if head is None: #when linked list ends, it is there! 
                return True
            
            if root is None: #when root ends
                return root == head
            
            if root.val != head.val: #value not equal 
                return False
            
            # check left and right subtree
            return isConnected(root.left,head.next) or isConnected(root.right,head.next)
        
        
        def helper(root):
            if not root:
                return False
            
            if root.val == head.val: ##if a values matches, check down the path
                if isConnected(root,head):
                    return True
                    
            # go through left and right subtree
            return helper(root.left) or helper(root.right)
        
        
        return helper(root)



'''
visited set + iteration + dfs
這邊用set 是為了防止重複拜訪
time: O(N)
space: O(N)
'''
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def listchk(head, root):
            if not head:
                return True
            if root and head.val == root.val:
                return (listchk(head.next, root.left) or
                        listchk(head.next, root.right))
            return False

        visited = set([])
        row = [root]
        while row:
            node = row.pop(0)
            visited.add(node)
            
            if node.val == head.val and listchk(head, node):
                return True
            if node.left and node.left not in visited:
                row.append(node.left)
            if node.right and node.right not in visited:
                row.append(node.right)

        return False