class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        counter = defaultdict(list)
        for s in strs:
            k = list(s)
            k = ",".join(sorted(k))
            counter[k].append(s)
        
        return list(counter.values())