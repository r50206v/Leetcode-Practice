class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph) - 1
        queue = [[0, i] for i in graph[0]]
        ans = []
        
        while queue:
            
            path = queue.pop(0)
            if path[-1]  == target:
                ans.append(path)
            else:
                for next_node in graph[path[-1]]:
                    queue.append(path + [next_node])
        
        return ans