import collections

def ValidBinarySearchTree(root):

    def dfs(root, mini, maxi):
        if root:
            if mini >= root.val or root.val > maxi:
                return False
            return dfs(root.left, mini, root.val) and dfs(root.right, root.val, maxi)
        return True
    
    return dfs(root, float("-inf"), float("inf"))


def ConstructBinaryTree(preorder, inorder):

    if len(preorder) != len(inorder):
        return None
    if len(preorder) == 0:
        return None
    
    root = Node(preorder[0])
    idx = inorder.index(preorder[0])
    
    root.left = self.ConstructBinaryTree(preorder[1: 1+idx], inorder[:idx])
    root.right = self.ConstructBinaryTree(preorder[1+idx:], inorder[idx+1:])
    return root


def FlattenBinaryTree(root):
    if not root:
        return root
    if not root.left and not root.right:
        return root
    
    leftTail = self.FlattenBinaryTree(root.left)
    rightTail = self.FlattenBinaryTree(root.right)

    if leftTail:
        leftTail.right = root.right
        root.right = root.left
        root.left = None
    
    if rightTail:
        return rightTail
    else:
        return leftTail


def PopulateNextRightPointers(root):
    if not root:
        return None

    queue = [root]
    while queue:
        level_size = len(queue)
        for i in level_size:
            node = queue.pop(0)
            if index < level_size - 1:
                node.next = queue[0]
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


def BinaryTreeRightsideValue(root):
    if not root:
        return None
    
    queue = collections.deque([root])
    ans = []
    while queue:

        level_size = len(queue)
        ans.append(queue[level_size - 1].val)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(right.right)
    return ans


def NumberOfIslands(grid):
    rowN = len(grid)
    colN = len(grid[0])

    count = 0
    for r in range(rowN):
        for c in range(colN):
            count += searchNeighbor(grid, r, c)
    return count


def searchNeighbor(grid, row, col):
    if row < 0 or row == len(grid):
        return 0
    if col < 0 or col == len(grid[0]):
        return 0

    if grid[row][col] == '0':
        return 0
    else:
        grid[row][col] = "0"
        searchNeighbor(grid, row+1, col)
        searchNeighbor(grid, row, col+1)
        searchNeighbor(grid, row-1, col)
        searchNeighbor(grid, row, col-1)
    return 1


def KSmallestElementInBST(root, k):
    # DFS with inorder
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right)
    
    return inorder(root)[k - 1]


def FindSecondMinimumValue(root):
    self.ans = float("inf")
    mini = root.val

    def dfs(r):
        if r:
            if mini <  r.val < self.ans:
                self.ans = r.val
            elif r.val == mini:
                dfs(r.left)
                dfs(r.right)
    dfs(root)
    return self.ans if self.ans < float("inf") else -1


def BinaryTreeVerticalOrder(root):
    if not root:
        return []

    colTable = collections.defaultdict(list)
    min_col = max_col = 0

    def dfs(node, r, c):
        if node:
            nonlocal min_col, max_col
            colTable[c].append(r, node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

    dfs(root, 0, 0)
    result = []
    for col in range(min_col, max_col+1, 1):
        colTable[col].sort(key=lambda x: x[0])
        colValue = [v[1] for v in colTable[col]]
        result.append(colValue)
    return result


def BinaryTreeZigZag(root):
    if not root:
        return []

    level_list = collections.deque([])
    queue = collections.deque([root, None])
    from_left = True
    result = []

    while queue:

        node = queue.popleft()
        if node:
            if from_left:
                level_list.append(node.val)
            else:
                level_list.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        else:
            result.append(level_list)
            if len(queue) > 0:
                queue.append(None)
            level_list = collections.deque([])
            from_left = not from_left
    return result


def FlattenMultilevelDoublyLinkedList(head):
    if not head:
        return head

    prev = None 
    stack = [head]
    while stack: 
        curr = stack.pop()

        if prev:
            prev.next = curr
        curr.prev = prev

        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr
    return head


def DecodeString(strs):

    result = ""
    strStack = []
    countStack = []
    base = ""

    for index in range(len(s)):

        if s[index].isdigit():
            base += s[index]
        elif s[index] == '[':
            strStack.append(result)
            result = ""
            
            countStack.append(int(base))
            base = ""
        elif s[index] == ']':
            result = strStack.pop() + (result * countStack.pop())
        else:
            result += s[index]
    return result


# 684. Redundant Connection
'''
Time: O(N**2)
Space: O(N)
dfs
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                else:
                    return any(dfs(nei, target) for nei in graph[source])
                
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            
            graph[u].add(v)
            graph[v].add(u)
        return -1, -1


# 684. Redundant Connection
'''
Time: O(N)
Space: O(N)
Disjoint Set with Kruskal's spanning tree method 
'''
class Solution(object):
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # using union find
        self.parent = [-1]*(len(edges)+1)   # -1 is giving me 98% time 
        
        def find(x):
            while self.parent[x] > 0:
                x = self.parent[x]
            return x     
        
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
        
            if root_x == root_y:
                return False
            else:
                self.parent[root_x] = root_y
                return True
            
        for u,v in edges:
            if not union(u,v):
                return [u,v]


# 1162 As Far From Land As Possible
'''
Time: O(N**2)
Space: O(N)
'''
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue, visited = [], set([])
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))
        
        if len(queue) == 0 or len(queue) == N**2:
            return -1
        ans = 0
        while queue:
            x, y, d = queue.pop(0)
            for x_d, y_d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (0 <= x + x_d <= N-1) and (0 <= y + y_d <= N-1):
                    if (x + x_d, y + y_d) not in visited:
                        visited.add((x + x_d, y + y_d))
                        queue.append((x + x_d, y + y_d, d + 1))
                        ans = max(ans, d + 1)
        return ans
                