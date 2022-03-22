'''
Sorting
time: O(NlogN)
space: O(N)
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        intervals.append([float("inf"), float("inf")])
        
        ans = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s <= end:
                end = max(end, e)
            else: 
                ans.append([start, end])
                start = s
                end = e
        return ans


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        ans = [intervals[0]]
        
        for inter in intervals[1:]:
            
            if ans[-1][1] < inter[0]:
                ans.append(inter)
                
            else:
                ans[-1][1] = max(ans[-1][1], inter[1])
                
        return ans