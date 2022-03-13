class Solution:
    def freqAlphabets(self, s: str) -> str:
        size = len(s)
        result = ""
        i = 0
        while i<size:
            if (i < size-2) and (s[i+2] == '#'):
                result += chr(int(s[i:i+2])+96)
                i += 3
            else:
                result += chr(int(s[i])+96)
                i += 1
        return result



class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = {str(ord(i)-96): i for i in string.ascii_letters}
        mapping[""] = ""
        mapping["0"] = ""
        mapping["00"] = ""
        
        if s[-1] != "#":
            s += "00#"
        
        ans = ""
        numsList = s.split("#")
        for n in numsList:
            
            tmp = ""
            if len(n) > 2:
                for i in n[:-2]:
                    tmp = tmp + mapping[i]
                tmp += mapping[n[-2:]]
            else:
                tmp += mapping[n]
            
            ans += tmp
            
        return ans