'''
time: O(logN)
space: O(N)
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([])
        
        def square_loop(n):
            if n not in visited:
                visited.add(n)
                
                sqList = [int(s)**2 for s in list(str(n))]
                total = sum(sqList)
                if total == 1:
                    return True
                return square_loop(total)
            else:
                return False
        
        return square_loop(n)