'''
dfs
time: O(V + E)
space: O(V)

a cycle-finding DFS algorithm on each node individually. 
We mark a node gray on entry, and black on exit. 
If we see a gray node during our DFS, 
it must be part of a cycle. 
In a naive view, we'll clear the colors between each search.
'''
import collections
class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != white:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))