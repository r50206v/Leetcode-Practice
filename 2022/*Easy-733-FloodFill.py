'''
bfs
time: O(N)
space: O(N)
'''
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        visited = set([])
        queue = deque([(sr, sc)])
        starting_color = image[sr][sc]
        
        while queue: 
            pos_r, pos_c = queue.popleft()
                
            if image[pos_r][pos_c] == starting_color:
                image[pos_r][pos_c] = newColor
            else:
                continue

            visited.add((pos_r, pos_c))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                curr_x, curr_y = pos_r + x, pos_c + y
                if 0 <= curr_x < len(image) and 0 <= curr_y < len(image[0]) and (curr_x, curr_y) not in visited:
                    queue.append((pos_r + x, pos_c + y))
            
        return image


'''
depth first search
time: O(N)
space: O(N)
'''
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image