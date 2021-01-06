def TwoSum(nums, target):

    hashmap = {target - v: i for i, v in enumerate(nums)}
    for index, n in enumerate(nums):

        if n in hashmap.keys():
            if index != hashmap[n]:
                return [index, hashmap[n]]
    return []


def LongSubstringWithoutRepeatCharacters(s):

    left = 0
    right = 0
    max_len = 0
    S = set()

    while right < len(s):

        current_char = s[right]
        if current_char not in S:
            S.add(current_char)
            max_len = max(max_len, len(S))
            right += 1
        else:
            S.remove(s[left])
            left += 1

    return max_len


def ThreeSum(nums):
    ansSet = set()
    nums = sorted(nums)

    for index in range(len(nums)):

        if index > 0 and nums[index] == nums[index - 1]:
            continue

        left = index + 1
        right = len(nums) - 1
        while left < right:
            current_ans = nums[index] + nums[left] + nums[right]
            if current_ans == 0:
                ansSet.add(nums[index], nums[left], nums[right])
                left += 1
                right -= 1
            else:
                if current_ans < 0:
                    left += 1
                else:
                    right -= 1
    return list(ansSet)


def ValidAnagram(s, t):

    s_count = collections.Counter(s)
    t_count = collections.Counter(t)
    if s_count == t_count:
        return True
    else:
        return False


def SpiralMatrix(matrix):

    if not matrix:
        return []

    def spiral_generator(r1, c1, r2, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1, r2 + 1):
            yield r, c2
        
        # we need to make sure not to provide the same number twice
        # 當在同一行or列的時候，我們就不用轉彎
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2 - 1, r1, -1):
                yield r, c1
        
    ans = []
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_generator(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans


def MergeSortedArray(nums1, m, nums2, n):
    # loop backward 
    # and fill larger value at the end of our sequence
    while m > 0 and n > 0:
        if nums1[m-1] > nums[n-1]:
            nums[m + n - 1] = nums1[m-1]
            m = m - 1
        else:
            nums[m + n - 1] = nums2[n-1]
            n = n - 1
    if n > 0:
        nums1[:n] = nums2[:n]


def generatePascalTriangle(numRows):

    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    ans = [[1], [1, 1]]
    prev = [1, 1]
    for row in range(3, numRows + 1):

        nextRow = [1]
        for index in range(1, len(prev)):
            nextRow.append(prev[index - 1] + prev[index])
        nextRow.append(1)

        prev = nextRow
        ans.append(nextRow)

    return ans


def MoveZeros(nums):

    j = 0
    for i in range(nums):

        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1


def FirstUniqueCharacterInString(s):

    hashmap = collections.defaultdict(lambda: 0)
    for i in s:
        hashmap[i] += 1
    
    ansIndex = float("inf")
    for char, count in hashmap.items():
        if count == 1:
            ansIndex = min(s.index(char), ansIndex)
    
    if ansIndex == float("inf"):
        return -1
    else:
        return ansIndex


def StringComparison(chars):
    anchor, write = 0, 0

    for read, c in enumerate(chars):
        # we do action when we are at the end of the string
        # and when the next char is different
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for d in str(read - anchor + 1):
                    chars[write] = d
                    write += 1
            anchor = read + 1
    return write


def SubarraySumEqualsK(nums, k):
    cumulation = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        cumulation[i] = cumulation[i - 1] + nums[i - 1]

    for i in range(len(nums)):
        for j in range(i+1, len(nums) + 1):
            if cumulation[j] - cumulation[i] == k:
                ans += 1
    return ans


def SubarraySumEqualsK(nums, k):
    d = collections.defaultdict(lambda: 0)
    d[0] = 1
    tmp_sum = 0
    res = 0

    for i in range(len(nums)):
        tmp_sum += nums[i]
        if tmp_sum - k in d:
            res += d[tmp_sum - k]
        d[tmp_sum] += 1
    return res


def CandyCrash(board):

    while True:

        crush = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if j > 1 and board[i][j] and board[i][j] == board[i][j-1] and board[i][j-2]:
                    crush.add({(i, j), (i, j-1), (i, j-2)})
                if i > 1 and board[i][j] and board[i][j] == board[i-1][j] and board[i-2][j]:
                    crush.add({(i, j), (i-1, j), (i-2, j)})
        
        if len(crush) == 0:
            break

        for i, j in crush:
            board[i][j] = 0
        
        for col in range(len(board[0])):
            idx = len(board) - 1

            for row in range(len(board)-1, -1, -1):
                if board[row][col] > 0:
                    board[idx][col] = board[row][col]
                    idx -= 1
                
            for row in range(idx + 1):
                board[row][col] = 0

    return board


def CandyCrash1D(s):

    stack = ['#']
    for i in s + '#':
        if i not in stack[-1] and len(stack[-1]) >= 3:
            stack.pop()

        if i in stack[-1]:
            stack[-1] += i
        else:
            stack.append(i)
    return "".join(stack[1:-1])


def BestTimeToBuyAndSellStock(prices):

    minBuy = prices[0]
    maxProfit = 0

    for p in prices:
        maxProfit = max(maxProfit, p - minBuy)
        minBuy = min(minBuy, p)
    return maxProfit


def IntegerToRoman(num):

    digits = {
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    }

    roman_digit = []
    for value, symbol in digits.items():
        if num == 0:
            break
        count, num = divmod(num, value)
        roman_digit.append(symbol * count)
    return "".join(roman_digit)


def Subsets(nums):
    n = len(nums)
    output = [[]]

    for i in nums:
        output.append([ c + [i] for c in output ])
    return output


# 316
# 1081
def RemoveDuplicateLetters(self, s) -> int:
    stack = []
    seen = set()
    last_occurrence = {c: i for i, c in enumerate(s)}

    for i, c in enumerate(s):
        if c not in seen:
            # if the last letter in our solution:
            #    1. exists
            #    2. is greater than c so removing it will make the string smaller
            #    3. it's not the last occurrence
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)


# 384 shuffle an array
'''
time: O(N)
space: O(N)
Fisher Yates Algorithm
proof of correctness:
P(1st)*P(2nd)*...*P(Nth)
= 1/n * 1/n-1 * ... * 1/1
= 1/(n!)
'''
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

'''
time: O(N**2) (one for the loop and one for the pop)
space: O(N)
Brute Force
the correctness proof:
P(the element e being chosen on the kth iteration)
= P(e is not chosen before 1~k-1th iter) * P(e is chosen at kth iteration)
= P(e is not chosen at 1st) * P(e is not chosen at 2nd| e not in 1st)*...* P(e not in k-1th| e not in k-2th) * P(e in kth)
= (n-1)/n * (n-2)/(n-1) * ... * (n-k)/(n-k+1) * P(e in kth)
= (n-k)/n * 1/n-k
= 1/n
-> this means every element has equal permutation 
'''
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array