# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

'''
N be the total number of integers within the nested list, 
L be the total number of lists within the nested list, 
and D be the maximum nesting depth (maximum number of lists inside each other)

iteration + stack
time: 
    construction: O(N + L)
    other operations: amortized time complexity O(L/N) or O(1)
space: O(N + L)
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))
    
    def next(self) -> int:
        self.make_stack()
        return self.stack.pop(-1).getInteger()
    
    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        
    def make_stack(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop(-1).getList()))
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

'''
recursion
time: 
    construction O(N + L)
    other operations: O(1)
space: O(N + D)
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList()) 
        self._integers = []
        flatten_list(nestedList)
    
    def next(self) -> int:
        return self._integers.pop(0)
        
    def hasNext(self) -> bool:
        return len(self._integers) > 0