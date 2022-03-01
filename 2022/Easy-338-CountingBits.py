'''
Pop Count Method
time: O(NlogN) 
space: O(1)
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        ans = []
        for b in range(n + 1):
            count = 0
            for i in bin(b)[2:]:
                if i == "1":
                    count += 1
            ans.append(count)
        return ans