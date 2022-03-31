'''
maintaining two stacks
time: O(1) for all operations
space: O(N)
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.min_value[-1]:
            self.min_value.append(val)

    def pop(self) -> None:
        val = self.stack.pop(-1)
        if val == self.min_value[-1]:
            self.min_value.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()