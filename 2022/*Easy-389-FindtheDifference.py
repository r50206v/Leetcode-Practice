class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        for k in t_counter.keys():
            if s_counter.get(k):
                t_counter[k] -= s_counter[k]
            else:
                return k
        
        for k in t_counter.keys():
            if t_counter[k] > 0:
                ans = k
        return ans