'''
Dynamic Programming 
If row == 0: This is the top of the triangle: it stays the same.
If col == 0: There is only one cell above, located at (row - 1, col).
If col == row: There is only one cell above, located at (row - 1, col - 1).
In all other cases: There are two cells above, located at (row - 1, col - 1) and (row - 1, col) .

=>
Initialize a variable smallestAbove to positive infinity:
If col > 0:
    Set smallestAbove to triangle[row - 1][col - 1].
If col < row:
    Set smallestAbove to be the min out of itself and triangle[row - 1][col].
Set triangle[row][col] to be itself plus smallestAbove. 
Return the minimum value in triangle[n - 1].

time: O(N**2)
space: O(N**2)
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])