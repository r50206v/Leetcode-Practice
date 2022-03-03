class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        pointer_s = 0
        pointer_t = 0
        while (pointer_s < len(s)) and (pointer_t < len(t)):
            if s[pointer_s] == t[pointer_t]:
                if pointer_s == len(s) - 1:
                    return True
                pointer_s += 1
            
            pointer_t += 1
        
        return False