'''
time: O(N*M)
space: O(N*M)
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if len(mat) == 0 or r*c != len(mat) * len(mat[0]):
            return mat
        
        result = [[0 for i in range(c)] for j in range(r)]
        rows, cols = 0, 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result[rows][cols] = mat[i][j]
                cols += 1
                if cols == c:
                    rows += 1
                    cols = 0
                    
        return result 
