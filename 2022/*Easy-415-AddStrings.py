class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        idx_1, idx_2 = len(num1)-1, len(num2)-1
        carry = 0
        ans = ""
        while idx_1 >= 0 or idx_2 >= 0:
            
            curr = carry
            if idx_1 >= 0:
                curr += int(num1[idx_1])
                
            if idx_2 >= 0:
                curr += int(num2[idx_2])
            
            carry = curr // 10 
            curr = curr % 10
            
            ans = str(curr) + ans
            idx_1 -= 1
            idx_2 -= 1
            
        if carry:
            ans = "1" + ans
            
        return ans