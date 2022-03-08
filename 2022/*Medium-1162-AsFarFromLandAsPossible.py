'''
bfs
time: O(N*M)
space: O(N*M)
'''
class Solution:
	def maxDistance(self, grid: List[List[int]]) -> int:
		stack=[]
		count=0
		n=len(grid)
		for i in range(n):
			for j in range(n):
				if grid[i][j]==1:
					count+=1
					stack.append((i,j,0))
		if not stack:
			return -1
		if count==n*n:
			return -1
		for i,j,d in stack:
			for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
				if 0<=x<n and 0<=y<n and grid[x][y]!=1:
					grid[x][y]=1
					stack.append((x,y,d+1))
		return stack[-1][-1]


