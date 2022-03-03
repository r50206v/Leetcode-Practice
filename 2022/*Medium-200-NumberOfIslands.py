'''
dfs
time: O(N*M)
space: O(N*M)
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRow = len(grid)
        numCol = len(grid[0])
        
        def dfs(r, c):
            if grid[r][c] == "1":
                grid[r][c] = 0
                
                if r + 1 < numRow: dfs(r+1, c)
                if r - 1 >= 0: dfs(r-1, c)
                if c + 1 < numCol: dfs(r, c+1)
                if c - 1 >= 0: dfs(r, c-1)
                
                return 1
            return 0
        
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans += dfs(r, c)
        return ans