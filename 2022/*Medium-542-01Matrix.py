'''
bfs
time: O(N*M)
space: O(N*M)
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []
        
        m, n = len(mat), len(mat[0])
        q = deque()
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                # neighbor
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]: # 4 directions
                    nx, ny = x + dx, y + dy # new x coordinate, new y coordinate
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        mat[nx][ny] = mat[x][y] + 1
        return mat