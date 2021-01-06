# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def findTarget(org, tar, ans=[]):
            if not org:
                return None
            if org.val == tar.val:
                return ans
            else:
                nextDirect = findTarget(org.left, tar, ['l']) or findTarget(org.right, tar, ['r'])
                if nextDirect:
                    return ans + nextDirect
                else:
                    return None
            
        def followRoute(cloned, route):
            while route:
                direct = route.pop(0)
                if direct == 'l':
                    cloned = cloned.left
                elif direct == 'r':
                    cloned = cloned.right
            return cloned
    
        route = findTarget(original, target)
        return followRoute(cloned, route)