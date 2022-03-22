class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        curr = 1
        rows = columns = n
        up = left = 0
        right = columns - 1
        down = rows - 1

        while curr <= n ** 2:
            # Traverse from left to right.
            for col in range(left, right + 1):
                matrix[up][col] = curr
                curr += 1

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                matrix[row][right] = curr
                curr += 1

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    matrix[down][col] = curr
                    curr += 1
            
            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    matrix[row][left] = curr
                    curr += 1
 
            left += 1
            right -= 1
            up += 1
            down -= 1
            
        return matrix