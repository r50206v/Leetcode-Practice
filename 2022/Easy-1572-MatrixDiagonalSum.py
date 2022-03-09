class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for row in range(len(mat)):
            c1, c2 = row, (len(mat[0])-1) - row
            if c1 == c2:
                ans += mat[row][c1]
            else:
                ans += mat[row][c1] + mat[row][c2]
        return ans