class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if self.dict.get(key):
            self.dict.move_to_end(key, last=True)
            return self.dict.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.dict.get(key):
            self.dict[key] = value
            self.dict.move_to_end(key, last=True)
        else:
            self.dict[key] = value
            if len(self.dict.keys()) > self.capacity:
                self.dict.popitem(last=False)


from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)