"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Depth First Search
'''
time: O(N + M) N is number of nodes and M is number of edges
space: O(N + H) H is the height of the graph, and is always smaller than N
'''
class Solution:
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return node
        
        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]
        
        # Create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])
        
        # The key is original node and value being the clone node.
        self.visited[node] = clone_node
        
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node


# Breadth First Search
'''
time: O(N + M) N is number of nodes and M is number of edges
space: O(N + W) W is the width of the graph, and is always smaller than N
'''
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        
        queue = deque([node])
        
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            for nei in n.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val, [])
                    queue.append(nei)
                
                visited[n].neighbors.append(visited[nei])
                
        return visited[node]