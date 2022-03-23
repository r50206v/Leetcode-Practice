class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        splitList = s.split(" ")
        pattern = list(pattern)
        
        if len(pattern) != len(splitList):
            return False
        
        mapping = {}
        rev_mapping = {}
        
        for p, string in zip(pattern, splitList):
            
            if mapping.get(p) and rev_mapping.get(string):
                if mapping[p] == string and rev_mapping[string] == p:
                    continue
                else:
                    return False
            elif mapping.get(p) and not rev_mapping.get(string):
                return False
            elif not mapping.get(p) and rev_mapping.get(string):
                return False
            else:
                mapping[p] = string
                rev_mapping[string] = p
                
        return True