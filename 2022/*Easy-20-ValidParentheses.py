class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        mapping = {'(': ')', '{': '}', '[': ']'}
        
        queue = []
        for v in s:
            if v in mapping.keys():
                queue.append(mapping[v])
            elif queue and v == queue[-1]:
                queue.pop(-1)
            else:
                return False
        
        if len(queue) != 0:
            return False
        return True