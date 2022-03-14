'''
We only need to count the nodes that have no incoming degree. 
Create a list of n numbers, 
then create a list of nodes with incoming degrees. Return their difference.
time: O(E)
space: O(N)
'''
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        q = [i for i in range(n)]
        p = [e[1] for e in edges]
        return list(set(q)-set(p))


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr = [0] * n
        ret = []
        
        for edge in edges:
            arr[edge[1]] = 1
            
        for i in range(n):
            if arr[i] == 0:
                ret.append(i)
                
        return ret