'''
dfs
time: O(N*M)
space: O(N*M)
'''
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if i == n or j == m or i < 0 or j < 0 or grid[i][j]:
                return
            
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i in (0, n-1) or j in (0, m-1)):
                    dfs(i, j)
        print(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    res += 1
        
        return res