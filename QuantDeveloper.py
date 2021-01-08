def MaximumSubArray(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    
    for index in range(1, len(nums)):
        dp[index] = max(dp[index - 1] + nums[index], nums[index])
        
    return max(dp))


# Time: O(N), Space: O(N)
def ShuffleAnArray(array):
    for i in range(len(array)):
        # uniformly choose from range [i, len(array)]
        swap_idx = random.randrange(i, len(array))
        array[i], array[swap_idx] = array[swap_idx], array[i]
    return array

# Time: O(N**2)
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)): # O(N)
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx) # O(N)
        return self.array


# ****** important
# Rejection Sampling
# Time: avg O(1), worst O(inf), Space: O(1)
def Rand10UsingRand7():
    x = 49
    while x > 40:
        col = rand7()
        row = (rand7() - 1) * 7
        x = col + row
    return 1 + (x - 1) % 10
# this method guarantees we will not generate 0


def Rand10UsingRand7():
    v1, v2 = rand7(), rand7()
    while v1 > 5: v1 = rand7()
    while v2 == 7: v2 = rand7()
    return v1 if v2 <= 3 else v1 + 5
'''
Since 49 is not a multiple of 10, we have to use rejection sampling. 
Our desired range is integers from 1 to 40, 
which we can return the answer immediately. 
If not (the integer falls between 41 to 49), 
we reject it and repeat the whole process again.

Exp(# of Rand7 call) = 2*40/49 + 4*9/49*40/49 + ...
each sample follows a geometric distribution with p = 40/49
Exp(# of Rand7 call) = 2 * 1/p = 2*49/40 = 2.45
'''



# ****** important
def RemoveDuplicatesFromSortedArray(nums):
    if len(nums) == 0:
        return 0
    
    ans = 0
    for i in range(1, len(nums)):
        if nums[ans] != nums[i]:
            nums[ans+1] = nums[i]
            ans += 1
    return ans + 1
            

def SubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    
    prod = 1
    ans = left = 0
    for right, val in enumerate(nums):
        prod *= val
        while prod >= k:
            prod /= nums[left]
            left += 1
        ans += right - left + 1
    return ans 


def IncreasingDecreasingString(s):
    result = ""
    length = len(s)
    
    while len(result) < length:
        sList = sorted(list(set(s)))
        for i in sList:
            result += i
            s = s.replace(i, "", 1)
        
        sList = sorted(list(set(s)))
        for i in sList[::-1]:
            result += i
            s = s.replace(i, "", 1)
            
    return result
            

# ****** important
# Newton's method
'''
x(n+1) = x(n) - f(xn) / f'(xn)
'''
def Sqrt(x):
    if x < 2:
        return x
    
    x0 = x
    x1 = (x0 + x / x0) / 2
    while abs(x0 - x1) >= 0.001:
        x0 = x1
        x1 = (x0 + x / x0) / 2
    return x1

# ****** important
# Gradient Descent
'''
x(n+1) = x(n) - r * f'(xn)
'''
def Sqrt(x):
    if x < 2:
        return x
    
    r = learning_rate
    x0 = x
    x1 = x0 - 2*r*x0
    while x1**2 - x >= 0.001:
        x0 = x1
        x1 = x0 - 2*r*x0
    return x1


# ****** important
def RotateMatrix(mat):
    N = len(mat)
    if N != len(mat[0]):
        raise Error('should be a square matrix')

    for x in range(0, int(N / 2)): 
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, N-x-1): 
            print(x, y)
            # store current cell in temp variable 
            temp = mat[x][y] 
            # move values from right to top 
            mat[x][y] = mat[y][N-1-x] 
            # move values from bottom to right 
            mat[y][N-1-x] = mat[N-1-x][N-1-y] 
            # move values from left to bottom 
            mat[N-1-x][N-1-y] = mat[N-1-y][x] 
            # assign temp to left 
            mat[N-1-y][x] = temp 
    return mat


# ****** important
def ReplaceIndexWithFilledValue(value_list, index_list, filled_list):
    '''输出一个新value list，其中在indices list里的element替换成filled_value'''
    for ind, val in zip(index_list, filled_list):
        value_list[ind] = val
    return value_list


# insert(value), get_max, get_mode, get_mean
import collections
class List(object):
    
    def __init__(self, nums):
        self.nums = nums
    
    def insert(self, index, value):
        try:
            if index == len(self.nums):
                self.nums.append(value)
            else:
                self.nums.insert(index, value)
        except:
            raise IndexError('exceed the existing index')
        
    def get_max(self):
        if len(self.nums) < 1:
            return None
        max_value = self.nums[0]
        for v in self.nums:
            if v > max_value:
                max_value = v
        return max_value
    
    def get_min(self):
        if len(self.nums) < 1:
            return None
        min_value = self.nums[0]
        for v in self.nums:
            if v < min_value:
                min_value = v
        return min_value
    
    def get_mode(self):
        if len(self.nums) < 1:
            return None
        
        countMap = collections.defaultdict(int)
        max_count = 0
        for v in self.nums:
            countMap[v] += 1
            if countMap[v] > max_count:
                max_count = countMap[v]
        
        mode = []
        for k, v in countMap.items():
            if v == max_count:
                mode.append(k)
        return mode


def AsFarFromLandAsPossible(grid):
    # bfs: visit all land first
    queue, visited = [], set([])
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                queue.append((i, j, 0))
                visited.add((i, j))
    
    if len(queue) == 0 or len(queue) == N**2:
        return -1
    ans = 0
    # go over all land if any neighbor is water than calculate the distance
    # compare with current max answer
    while queue:
        x, y, d = queue.pop(0)
        for x_d, y_d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (0 <= x + x_d <= N-1) and (0 <= y + y_d <= N-1):
                if (x + x_d, y + y_d) not in visited:
                    visited.add((x + x_d, y + y_d))
                    queue.append((x + x_d, y + y_d, d + 1))
                    ans = max(ans, d + 1)
    return ans
            

# Moving Average
'''
Time: O(1)
Space: O(N)
'''
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        
        self.count += 1
        self.queue.append(val)
        if self.count > self.size:
            tail = self.queue.pop(0)
        else:
            tail = 0
            
        self.window_sum = self.window_sum + val - tail
        return self.window_sum / min(self.size, self.count)


# 16 threeSumClosest
'''
two pointer
time: O(N**2 + NlogN)
space: O(N) or O(logN) [depending on the implementation of sorting algorithm]
If an interviewer asks you whether you can achieve O(1) memory complexity, 
you can use the selection sort instead of a built-in sort in the Two Pointers approach. 
It will make it a bit slower, though the overall time complexity will be still O(n^2).
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()

        for i in range(len(nums)):
            low, high = i + 1, len(nums) - 1
            
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if abs(target - three_sum) < abs(diff):
                    diff = target - three_sum
                    
                if three_sum < target:
                    low += 1
                else:
                    high -= 1
                    
            if diff == 0:
                break
        
        return target - diff

    

# 833. Find And Replace in String
'''
time: O(NM + N) M is the length of each targets 
if the indexes is incremental, otherwise it takes O(NlogN + NM) to sort the indexes
space: O(N)
'''
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        
        S = list(S)
        for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
            print(i, x, y)
            
            if all(i + k < len(S) and S[i + k]==x[k] for k in range(len(x))):
                S[i:i+len(x)] = list(y)
        
        return "".join(S)


# 5 Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s):
        longest_palindrom = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        #filling out the diagonal by 1
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrom = s[i]
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : 
                # to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  #if the chars mathces
                    # if len slicied sub_string is just one letter
                    # if the characters are equal, 
                    # we can say they are palindomr dp[i][j] =True 
                    #if the slicied sub_string is longer than 1, 
                    # then we should check if the inner string is also palindrom 
                    # (check dp[i+1][j-1] is True)
                    if j-i ==1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if len(longest_palindrom) < len(s[i:j+1]):
                            longest_palindrom = s[i:j+1]
                
        return longest_palindrom


# 259. 3Sum Smaller
'''
time: O(N**2)
space: O(1)
'''
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                three_sum = nums[i] + nums[low] + nums[high]
                if three_sum < target:
                    ans += high - low
                    low += 1
                else:
                    high -= 1
                    
        return ans


# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = collections.Counter(s)
        t_count = collections.Counter(t)
        if s_count == t_count:
            return True
        else:
            return False


# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'{': '}', '[': ']', '<': '>', '(': ')'}

        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False
        if s[0] in mapping.values():
            return False

        stack = []
        for p in s:
            if p in mapping.keys():
                stack.append(mapping[p])
            elif len(stack) != 0 and p == stack[-1]:
                stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
            return False


# 501. Find Mode in Binary Search Tree
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        counter = defaultdict(int)
        
        def dfs(tree, counter):
            if tree:
                counter[tree.val] += 1
                dfs(tree.left, counter)
                dfs(tree.right, counter)
        
        dfs(root, counter)
        max_count = -1
        mode_number = []
        for k, v in counter.items():
            if v > max_count:
                max_count = v
                mode_number = [k]
            elif v == max_count:
                mode_number.append(k)
                        
        return mode_number


# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for sub_s in s:
            if sub_s.isalnum():
                string += sub_s.lower()
        
        return string == string[::-1]



'''1. 口頭run example 的時候把數字都打出來
2. 太緊張
3. limitation 問清楚
4. 如果有用到演算法 就要提一下time complexity


1. 有打出來你的見解
2. 有給出一個edge case

1. 可以說一下你要用什麼data structure (queue or stack for bfs)
    你沒有說出data structure 就會讓我有點懷疑是不是在想用dfs
2. dfs / bfs'''


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



# 341. Flatten Nested List Iterator
'''
time: 
    constructor O(N + L) total N loops and plus L integers
        // the depth of nested list wont affect the time complexity
        // 因為永遠只有 N 個elements
    next O(1)
    hasNext O(1)
space:
    O(N + D) 每次在recursion 的時候都會產生一個stack
    D 指的是 the depth of nested list
'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        def flatten(nestedList):
            for n in nestedList:
                if n.isInteger():
                    self.flattenList.append(n)
                else:
                    flatten(n.getList())
        
        self.nestedList = nestedList
        self.flattenList = []
        self.callCount = 0
        flatten(nestedList)
    
    def next(self) -> int:
        self.callCount += 1
        return self.flattenList[self.callCount - 1]
        
    def hasNext(self) -> bool:
        if self.callCount < len(self.flattenList):
            return True
        else:
            return False


'''
Constructor: O(1)

In the constructor, we only create a generator object. 
Simply creating a generator object doesn't invoke any code
in the generator function itself (only calls to next do).
Because the time taken to create the generator doesn't 
vary with the size of the input, the time complexity is O(1)O(1).

next() / hasNext(): O(N/N + L/N) => O(L/N) or O(1)


'''
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        # Get a generator object from the generator function, passing in
        # nestedList as the parameter.
        self._generator = self._int_generator(nestedList)
        # All values are placed here before being returned.
        self._peeked = None

    # This is the generator function. It can be used to create generator
    # objects.
    def _int_generator(self, nested_list) -> "Generator[int]":
        # This code is the same as Approach 1. It's a recursive DFS.
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                # We always use "yield from" on recursive generator calls.
                yield from self._int_generator(nested.getList())
        # Will automatically raise a StopIteration.
    
    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext(): return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer
        
    def hasNext(self) -> bool:
        if self._peeked is not None: return True
        try: # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except: # The generator is finished so raised StopIteration.
            return False



# 380. Insert Delete GetRandom O(1)
'''
Time complexity. 
    GetRandom is always O(1). 
    Insert average O(1) worst case O(N)
    Delete average O(1) worst case O(N) 
    when the operation exceeds the capacity of currently allocated array/hashmap 
    and invokes space reallocation.

Space complexity: O(N), to store N elements.
'''
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_element, index = self.list[-1], self.dict[val]
            self.list[index] = last_element
            self.dict[last_element] = index
            self.list.pop(-1)
            del self.dict[val]
            return True
        return False
        
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        output = []
        backtrack(0)
        return output


# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        point1 = head
        point2 = head.next
        
        while point1 or point2:
            if point1 == point2:
                return True
            
            if point1.next:
                point1 = point1.next
            else:
                break
            if point2.next and point2.next.next:
                point2 = point2.next.next
            else:
                break
            
        return False
    

# 509. Fibonacci Number
'''
time: O(N)
space: O(N)
'''
class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1]
        if n <= 1:
            return arr[n]
        
        for i in range(2, n + 1):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[-1]