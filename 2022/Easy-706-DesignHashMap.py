'''
time: O(N)
space: O(N)
'''
class MyHashMap:

    def __init__(self):
        self.valueList = []
        self.keyList = []

    def put(self, key: int, value: int) -> None:
        if key in self.keyList:
            self.valueList[self.keyList.index(key)] = value
        else:
            self.keyList.append(key)
            self.valueList.append(value)

    def get(self, key: int) -> int:
        if key in self.keyList:
            return self.valueList[self.keyList.index(key)]
        return -1
                
    def remove(self, key: int) -> None:
        if key in self.keyList:
            pos = self.keyList.index(key)
            self.valueList[pos] = -1
            self.keyList[pos] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



'''
Modulo + Array
time: O(N/K)
space: O(K + M)

K is the number of predefined buckets
M is the number of unique keys
'''
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]


class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # better to be a prime number, less collision
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)