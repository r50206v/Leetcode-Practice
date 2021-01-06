# 1640. Check Array Formation Through Concatenation
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        i = 0
        hashmap = {p[0]: p for p in pieces}
        
        while i < n:
            if hashmap.get(arr[i]):           
                for x in hashmap[arr[i]]:
                    if x != arr[i]:
                        return False
                    i += 1
            else:
                return False
                
        return True