'''
time: 
    init O(N)
    convertAbb O(1)
    isUnique O(1) or O(N)
space: O(N)
'''

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.reverseMap = collections.defaultdict(list)
        self.countMap = collections.defaultdict(int)
        
        for d in dictionary:
            abb = self.convertAbb(d)
            self.reverseMap[abb].append(d)
            self.countMap[abb] += 1

    def convertAbb(self, word):
        if len(word) > 2:
            return word[0] + str(len(word) - 2) + word[-1]
        else:
            return word
    
    def isUnique(self, word: str) -> bool:
        abb = self.convertAbb(word)
        if self.countMap[abb] == 0:
            return True
        elif all(a == word for a in self.reverseMap[abb]):
            return True
        else:
            return False
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)