'''
time: O(N)
space: O(1)
greedy algorithm
While traversing over the nutsnuts array and adding the to-and-fro distance, 
we find out the saving, dd, which can be obtained if the squirrel goes to the
current nut first. Out of all the nuts, 
we find out the nut which maximizes the saving and then deduct this maximum saving 
from the sum total of the to-and-fro distance of all the nuts.
'''

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        max_saving = -inf
        sqx, sqy = squirrel 
        tx, ty = tree
        total_cost = 0
        for i, (x, y) in enumerate(nuts):
            nut_to_sqr = abs(x - sqx) + abs(y - sqy)
            nut_to_tree = abs(x - tx) + abs(y - ty)
            total_cost += nut_to_tree * 2
            saving = nut_to_tree - nut_to_sqr
            max_saving = max(max_saving, saving)
        return total_cost - max_saving