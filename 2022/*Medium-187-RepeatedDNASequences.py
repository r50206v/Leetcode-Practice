'''
Linear-time Slice Using Substring + HashSet
L is the constant length = 10
time: O((N-L) * L)
space: O((N-L) * L)
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import Counter
        seen = Counter([])
        for idx in range(len(s)-10+1):
            substr = s[idx:idx+10]
            seen[substr] += 1

        ans = []
        for k, v in seen.items():
            if v >= 2:
                ans.append(k)
        return ans