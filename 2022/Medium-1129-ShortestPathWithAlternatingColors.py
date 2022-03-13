'''
bfs
time: O(V)
space: O(V)
'''
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        for redFr, redTo in redEdges:
            graph[redFr].append((redTo, "R"))
        for blueFr, blueTo in blueEdges:
            graph[blueFr].append((blueTo, "B"))
        
        queue = collections.deque([(0, 'N', 0)]) # node, color, steps
        ans = [-1] * n
        ans[0] = 0
        visited = set()
        while queue:
            node, colorNode, stepsNode = queue.popleft()
            visited.add((node, colorNode))
            for neigh, colorNeigh in graph[node]:
                if colorNeigh != colorNode and (neigh, colorNeigh) not in visited:
                    steps = stepsNode + 1
                    if ans[neigh] == -1:
                        ans[neigh] = steps 
                    queue.append((neigh, colorNeigh, steps))
        return ans