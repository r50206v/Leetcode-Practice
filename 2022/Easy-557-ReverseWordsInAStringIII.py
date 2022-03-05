class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split(" ")
        result = []
        
        for sub_str in sList:
            result.append(sub_str[::-1])
            
        return " ".join(result)