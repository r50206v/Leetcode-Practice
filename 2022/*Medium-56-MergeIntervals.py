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