class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        N = len(mat)
        if mat == target:
            return True
        
        # rotate 90 degree
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = mat[i][j]
                mat[i][j] = mat[N - 1 - j][i]
                mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
                mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
                mat[j][N - 1 - i] = temp
        if mat == target:
            return True
        
        # rotate 180 degree
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = mat[i][j]
                mat[i][j] = mat[N - 1 - j][i]
                mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
                mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
                mat[j][N - 1 - i] = temp
        if mat == target:
            return True
        
        # rotate 240 degree
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = mat[i][j]
                mat[i][j] = mat[N - 1 - j][i]
                mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j]
                mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i]
                mat[j][N - 1 - i] = temp
        if mat == target:
            return True
        else:
            return False
        