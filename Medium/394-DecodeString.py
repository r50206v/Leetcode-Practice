'''
Iteration + 2 Stack
Time: O(N)
Space: O(m + n)
m: the number of letters in s
n: the number of numbers in s
'''


class Solution:
    def decodeString(self, s: str) -> str:
        
        result = ""
        strStack = []
        countStack = []
        base = ""
        
        for index in range(len(s)):
            
            if s[index].isdigit():
                base += s[index]
            
            elif s[index] == '[':
                strStack.append(result)
                result = ""
                
                countStack.append(int(base))
                base = ""
                
            elif s[index] == ']':
                print(strStack, countStack, result)
                # very important !!
                result = strStack.pop()  + (result * countStack.pop())
            
            else:
                result += s[index]
                
        return result
    