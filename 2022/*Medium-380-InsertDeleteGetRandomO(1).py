'''
if only hashmap -> random pick is O(N)
if only array -> delete is O(N)
combine two data structure

time: avg O(1), worst case is O(N) when O(N) the operation exceeds the 
capacity of currently allocated array/hashmap and invokes space reallocation.
space: O(N)
'''

class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            last_element, idx = self.array[-1], self.hashmap[val]
            self.array[idx], self.hashmap[last_element] = last_element, idx
            
            self.array.pop()
            del self.hashmap[val]
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        from numpy.random import choice
        pick = choice(self.array)
        return pick


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()