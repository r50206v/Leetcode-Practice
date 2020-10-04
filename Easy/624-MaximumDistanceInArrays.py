

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minNum = arrays[0][0]
        maxNum = arrays[0][-1]
        res = 0
        
        for i in range(1, len(arrays)):
            
            res = max(res, abs(maxNum - arrays[i][0]), abs(arrays[i][-1] - minNum))
            maxNum = max(maxNum, arrays[i][-1])
            minNum = min(minNum, arrays[i][0])
        
        
        return res