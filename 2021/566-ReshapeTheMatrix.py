class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        org_r, org_c = len(mat), len(mat[0])
        
        if org_r*org_c != r*c:
            return mat
        
        new_mat = [[0 for x in range(c)] for y in range(r)]
        count = 0
        for i in range(org_r):
            for j in range(org_c):
                new_mat[count // c][count % c] = mat[i][j]
                count += 1
        return new_mat