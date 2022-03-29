'''
sliding window with hashmap
time: O(Np + Ns)
space: O(K)
pCount and sCount will contain at most K elements each
'''
class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        set_s = Counter(list(s[-1*len(p):]))
        set_p = Counter(list(p))
        
        last_idx = len(s) - 1
        ans = []
        for idx in range(len(s)-len(p)-1, -1, -1):
            if set_s == set_p:
                ans.append(idx + 1)
                
            set_s[s[last_idx]] -= 1
            if set_s[s[last_idx]] == 0:
                del set_s[s[last_idx]]
            
            set_s[s[idx]] += 1
            last_idx -= 1
        
        if set_s == set_p:
            ans.append(0)
            
        return ans


'''
sliding window with array
time: O(Ns+Np)
space: O(K)
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count, s_count = [0] * 26, [0] * 26
        # build reference array using string p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1
        
        output = []
        # sliding window on the string s
        for i in range(ns):
            # add one more letter 
            # on the right side of the window
            s_count[ord(s[i]) - ord('a')] += 1
            # remove one letter 
            # from the left side of the window
            if i >= np:
                s_count[ord(s[i - np]) - ord('a')] -= 1
            # compare array in the sliding window
            # with the reference array
            if p_count == s_count:
                output.append(i - np + 1)
        
        return output