class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def get_neighbors(i, j):
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < N and 0 <= nj < N:
                    yield ni, nj

        # Find a piece of an island
        start = None
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        # BFS to find perimeter around one island
        q = deque([start])
        seen = set()
        water = set()
        while q:
            i, j = q.popleft()
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for ni, nj in get_neighbors(i, j):
                if grid[ni][nj] == 0:
                    water.add((ni, nj))
                else:
                    q.append((ni, nj))

        # BFS from the perimeter out, until the other island is reached
        q = deque(water)
        res = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                if grid[i][j] == 1:
                    return res
                for ni, nj in get_neighbors(i, j):
                    if (ni, nj) in seen:
                        continue
                    seen.add((ni, nj))
                    q.append((ni, nj))
            res += 1