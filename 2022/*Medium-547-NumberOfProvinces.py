class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # the graph is a adjacency matrixes
        graph = isConnected

        if not graph:
            return 0
         
        nodes = set(range(len(graph)))
        provinces = 0
        seen = set()
        
        for node in range(len(graph)):
            
            if node in seen:
                continue
                
            # start to perform bfs for each source
            seen.add(node)
            q = deque([node])

            while q:

                current = q.pop()
                # possible neighbors are the nodes not yet been visited
                for other in nodes - seen:

                    # search both edge
                    if graph[current][other] or graph[other][current]:
                        seen.add(other)
                        q.appendleft(other)

            # current traversal finished
            provinces += 1
                
        return provinces