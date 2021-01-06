'''
loop + stack
time: O(N)
space: O(N)
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directList = path.split("/")
        newList = []
        for d in directList:
            
            if d == '.' or d == '':
                continue
            elif d == '..':
                if len(newList) > 0:
                    newList.pop(-1)
            else:
                newList.append(d)
        
        return "/" + "/".join(newList)