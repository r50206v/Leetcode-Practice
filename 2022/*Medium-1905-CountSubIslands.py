class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS = len(grid1)
        COLS = len(grid1[0])
        
        visited = set()
        
        def dfs(r,c):
            # base case - just because we found water in grid2 does not mean that this island is not a sub-island
            #  - we will eventually reach the edge of the island
			# these conditions do not eliminate the possibility of the current island we're on being a sub-island
            if (r < 0 or c < 0 or r == ROWS or c == COLS or grid2[r][c] == 0 or (r,c) in visited):
                return True
            
            # if we passed our base case, then we have not visited these coordinates before and must add it to our set
            visited.add((r,c))
            
            res = True 
            # we don't want to return res immediately b/c we want to still want to visit the entirity of 
            # the island we're at in grid2 & later on we will search in all 4 directions.
			# this condition will eliminate the possibilty of the current island being a sub-island
			# if we did NOT return in the first if statement that means grid2 IS LAND (grid2[r][c] == 1) 
            # AND if grid1[r][c] == 0, then we know it is not a sub-island
            if (grid1[r][c] == 0):
                res = False
            
            # we explore in the 4 possible directions and if any one of these directions 
            # we find a cell in grid2 that is land, but is water in grid1. What we assumed to be a sub-island is no longer a sub-island
            # so if any of these 4 dfs function calls returns false - 
            # then we will ultimately return False b/c all it takes is 1 missing cell in grid1 
            res = dfs(r + 1, c) and res 
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            
            return res
            
        
        count = 0
        # explore every single position in the grid
        for r in range(ROWS):
            for c in range(COLS):
				# we want to run dfs on a coordinate that is land (condition1)
                # we need to make sure the coordinate we're at hasn't already been visited (c2)
				# we need to make sure that every cell in the island in grid2 is also available in the island in grid1 (c3)
                if grid2[r][c] == 1 and (r,c) not in visited and dfs(r,c):
                    count += 1
        
        return count