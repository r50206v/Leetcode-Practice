'''
greedy sorted array
time: O(NlogN)
space: O(1)
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x:(x[0],-x[1]))
        
        END = 1
        START = 0
        
        count = 0

        prev = intervals[0]
        ans = []
        for curr in intervals[1:]:

            if prev[END] > curr[START]:
                count+=1
                prev = [curr[START],min(prev[END],curr[END])]
            else:
                prev = curr
                ans.append(prev)
        return count


'''
greedy sorted array with stack
time: O(NlogN)
space: O(N)
'''
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        stack, res = [], 0
        intervals.sort()
        for interval in intervals:
            if stack and stack[-1][1] > interval[0]: 
                if stack[-1][1] > interval[1]:
                    stack.pop()
                    stack.append(interval)
                res += 1
            else:
                stack.append(interval)
            #print(stack)
        return res