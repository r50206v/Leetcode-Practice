class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        sr, sc = entrance   #starting row, starting column
        
        visited = {(sr,sc)}
        q = deque([(sr,sc,0)])  # 0 = initial distance
        
        while q:
            x, y, d = q.popleft()   # d = distance
            
            for dx, dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0 <= dx < rows and 0 <= dy < cols and (dx,dy) not in visited and maze[dx][dy] == ".":
                    visited.add((dx,dy))
                    q.append((dx,dy,d+1))
                    
                    if dx == 0 or dx == rows - 1 or dy == 0 or dy == cols - 1:  # check if reached the border
                        return d + 1
            
        
        return -1