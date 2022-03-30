class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        counter = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5: 
                counter[5] += 1
            elif i == 10 and counter[5] >= 1:
                counter[5] -= 1
                counter[10] += 1
            elif i == 20 and counter[10] >= 1 and counter[5] >= 1:
                counter[5] -= 1
                counter[10] -= 1
                counter[20] += 1
            elif i == 20 and counter[10] == 0 and counter[5] >= 3:
                counter[5] -= 3
                counter[20] += 1
            else:
                return False
        return True