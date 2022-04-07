'''
recursion
time: O(N*M)
space: O(N)
'''
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def dfs(array):
            if len(array) == 1:
                return array[0]
            
            tmp_k = k % len(array)
            new_length = len(array) - 1
            new_array = array[tmp_k:] + array[:(tmp_k-1)]
            new_array = new_array[:new_length]
            return dfs(new_array)
        
        return dfs(list(range(1,n+1)))