class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        m_counter = Counter(magazine)
        r_counter = Counter(ransomNote)
        for k in r_counter.keys():
            if m_counter.get(k):
                if m_counter[k] >= r_counter[k]:
                    continue
                else: 
                    return False
            else:
                return False
        return True
                    