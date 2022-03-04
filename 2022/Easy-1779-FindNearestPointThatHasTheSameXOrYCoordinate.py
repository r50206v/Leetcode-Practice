class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        curr = float("inf")
        
        for idx, p_list in enumerate(points):
            p_x, p_y = p_list
            if x == p_x or y == p_y:
                if curr > abs(x-p_x) + abs(y-p_y):
                    ans = idx
                    curr = abs(x-p_x) + abs(y-p_y)
        return ans