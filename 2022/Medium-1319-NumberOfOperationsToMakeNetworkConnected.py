'''
dfs
time: O(V*E)
space: O(V*E)
'''
class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # impossible to make all the computers connected if less than (n -1) connections
        if len(connections) < n - 1:
            return -1
			
        numOfClusters = 0
        self.visited = set() # Record the visited computer
        graph = defaultdict(list) # The graph of connected computers
        
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        def DFS(index):
            for j in graph[index]:
                if j not in self.visited:
                    self.visited.add(j)
                    DFS(j)
            
        for i in range(n):
            if i not in self.visited:
                DFS(i)
                numOfClusters += 1

        return numOfClusters - 1  # numOfClusters - 1 = number of isolated clusters