class MatchEngine:
    def __init__(self):
        self.set = set([])
        
    def one_get_one_word(self, word):
        return word.split(' ')
        
    def two_get_one_word(self, word):
        return word.split(' ')
        
    def comparison_engine(self, sentence1, sentence2):
        self.set = self.set.union(set(self.one_get_one_word(sentence1)))
        ans = []
        for w in self.two_get_one_word(sentence2):
            if w in self.set:
                ans.append(w)
        return ans


if __name__ == "__main__":
    x = MatchEngine()
    one = 'I have a fox'
    second = 'fox is runing'
    print(x.comparison_engine(one, second))
    '''
    >>> ['fox']
    '''