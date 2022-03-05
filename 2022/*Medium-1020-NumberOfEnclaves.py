class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        # We will first count total number of 1's and 
		# then those 1's which we can visit from boundaries will be removed.
        # So our answer will be = Total - Removed
        total = 0
        row = len(grid)
        col = len(grid[0])
        for x in grid:
            total += sum(x)



        # We will use this function to traverse from each cell to its adjacent cell
        # and whenever we step onto a cell containing 1 we will remove it
        # so that it prevents further loops or repeatations as we are using recursion

        def explore(x: int, y: int) -> int:
            # BASE CASE:
            # 1. If the cell we are visiting goes out of bound      ->we return 0 , means we got nothing
            # 2. If the cell currently we are on doesn't contain 1  -> we return 0
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == 0:
                return 0

            # 3. If there is a cell which contain 1, then at first we will make it zero [TO PREVENT REPEATATIONS]
            #   and we will return adjacent cell results i.e (x-1,y),(x+1,y),(x,y-1),(x,y+1)
            #   and one extra 1 because we just REMOVED ONE cell
            grid[x][y] = 0
            return 1 + explore(x-1, y) + explore(x+1, y) + explore(x, y-1) + explore(x, y+1)



        # Here we are searching the boundary only or you can say the 4 edges of the matrix
        removed = 0
        for i in range(row):
            if i == 0 or i == row-1:
                for j in range(col):
                    removed += explore(i, j)
            else:
                removed += explore(i, 0) + explore(i, len(grid[0])-1)

        # remaining 1's are the answer
        return total - removed