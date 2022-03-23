'''
merging the sorting intervals
time: O(NlogN)
space: O(N)
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pool = defaultdict(list)
        for i,x in enumerate(s):
            pool[x].append(i)
        
        merged = []
        maxNum = -1
        for x in pool.values():
            if x[-1] < maxNum:
                continue
            maxNum = max(maxNum, x[-1])
            if not merged or x[0] > merged[-1][1]:
                merged.append([x[0],x[-1]])
            else:
                merged[-1][1] = max(merged[-1][1], x[-1])
        return [d[-1]-d[0]+1 for d in merged]

'''
greedy
time: O(N)
space: O(1), there is only 26 chars in maximum
'''
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            
        return ans