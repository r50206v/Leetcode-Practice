'''
dfs
time: O(N*M)
space: O(N*M)
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
        
        def dfs(r, c, curr=0):
            if grid[r][c] == 1:
                curr += 1
                grid[r][c] = 0
                
                if r + 1 < numRow: curr += dfs(r+1, c)
                if r - 1 > -1: curr += dfs(r-1, c)
                if c + 1 < numCol: curr += dfs(r, c+1)
                if c - 1 > -1: curr += dfs(r, c-1)
                return curr
            return 0
        
        ans = 0
        for idx_r in range(len(grid)):
            for idx_c in range(len(grid[0])):
                
                ans = max(ans, dfs(idx_r, idx_c))
        return ans 