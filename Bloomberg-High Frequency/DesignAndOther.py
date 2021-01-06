import collections

'''
1. get the key / check if the key exist
2. put the key
3. delete the first added key
'''
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key): 
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


'''
maintain cumulative sum
'''
class MovingAverage:
    def __init__(self, size):
        self.max_window_size = size
        self.stream_data = []
        self.cumu_sum = 0
    
    def next(self, val):
        n = len(self.stream_data) 
        if n < self.max_window_size:
            self.stream_data.append(val)
            self.cumu_sum += val
        else:
            self.cumu_sum = self.cumu_sum - self.stream_data[0] + val
            self.stream_data.pop(0)
            self.stream_data.append(val)
        return self.cumu_sum / n


def ReverseInteger(x):
    if x > 0:
        result = int(str(x)[::-1])
    else:
        result = -1 * int(str(abs(x))[::-1])
    
    if abs(result) > 2**31:
        return 0
    else:
        return result


def WordSearch(board, word):
    self.board = board
    self.rowNum = len(board)
    self.colNum = len(board[0])

    for i in range(self.rowNum):
        for j in range(self.colNum):
            if self.dfs(i, j, word):
                return True
    return False

def dfs(r, c, suffix):

    if len(suffix) == 0:
        return True

    if r < 0 or r == self.rowNum:
        return False
    if c < 0 or c == self.colNum: 
        return False

    if board[r][c] != suffix[0]:
        return False

    ans = False
    self.board[r][c] = '$'
    for r_offset, c_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ans = self.dfs(row + r_offset, c + c_offset, suffix[1:])
        if ans:
            break

    self.board[r][c] = suffix[0]
    return ans