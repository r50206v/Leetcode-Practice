class Solution:
    def simplifyPath(self, path: str) -> str:
        dirList = path.split('/')
        ans = []
        for d in dirList:
            if d in ('.', ''):
                continue
            elif d == '..' and len(ans) > 0:
                ans.pop(-1)
            elif d == '..' and len(ans) == 0:
                continue
            else:
                ans.append(d)
        return "/" + "/".join(ans)