# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 0:
            return 0
        
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[ans]:
                nums[ans+1] = nums[i]
                ans += 1
        return ans + 1


# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                ans += prices[i + 1] - prices[i]
        return ans


# 189. Rotate Array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        
        nums[:] = nums[-k:] + nums[:-k]
        

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False


# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common()[-1][0]


# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_intersect(long, short):
            ans = set([])
            for s in short:
                if s in long:
                    ans.add(s)
            return ans
        
        if len(nums1) > len(nums2):
            return get_intersect(nums1, nums2)
        else:
            return get_intersect(nums2, nums1)


# 350. Intersection of Two Arrays II
# time: O(n*m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_intersect(long, short):
            ans = []
            for s in short:
                if s in long:
                    ans.append(s)
                    long.pop(long.index(s))
            return ans
        
        if len(nums1) > len(nums2):
            return get_intersect(nums1, nums2)
        else:
            return get_intersect(nums2, nums1)


# 350. Intersection of Two Arrays II
# time: O(n + m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def get_intersect(long, short):
            hashmap = collections.Counter(long)
            ans = []
            for s in short:
                if hashmap.get(s):
                    if hashmap[s] > 0:
                        ans.append(s)
                        hashmap[s] -= 1
            return ans
            
        
        if len(nums1) > len(nums2):
            return get_intersect(nums1, nums2)
        else:
            return get_intersect(nums2, nums1)



# 	66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        
        if carry:
            ans = []
            for d in digits[::-1]:
                ans.append((d + carry) % 10)
                carry = (d + carry) // 10
            if carry:
                return [carry] + ans[::-1]
            return ans[::-1]
        else:
            digits[-1] = digits[-1] + 1
            return digits


# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            
            if nums[i] != 0:
                
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                
                
# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        org = {target - value: index for index, value in enumerate(nums)}
        
        for index, value in enumerate(nums):
            if org.get(value) is not None:
                if org[value] != index:
                    return [org[value], index]
        return None


# 48. rotate image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N != len(matrix[0]):
            raise ValueError('not a square matrix')
            
        for x in range(0, int(N/2)):
            for y in range(x, N-x-1):
                
                temp = matrix[x][y]
                matrix[x][y] = matrix[N-y-1][x]
                matrix[N-y-1][x] = matrix[N-x-1][N-y-1]
                matrix[N-x-1][N-y-1] = matrix[y][N-x-1]
                matrix[y][N-x-1] = temp
                
        return matrix


# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowN = len(board)
        colN = len(board[0])
        
        for r in range(rowN):
            rowSet = set([])
            for c in range(colN):
                if board[r][c] in rowSet:
                    return False
                elif board[r][c] != ".":
                    rowSet.add(board[r][c])
        
        for c in range(colN):
            colSet = set([])
            for r in range(rowN):
                if board[r][c] in colSet:
                    print('here2')
                    return False
                elif board[r][c] != ".":
                    colSet.add(board[r][c])
        
        for r in range(0, rowN, 3):
            for c in range(0, colN, 3):
                
                subSet = set([])
                for r_sub in [r, r+1, r+2]:
                    for c_sub in [c, c+1, c+2]:
                        if board[r_sub][c_sub] in subSet:
                            print('here3')
                            return False
                        elif board[r_sub][c_sub] != ".":
                            subSet.add(board[r_sub][c_sub])
        return True