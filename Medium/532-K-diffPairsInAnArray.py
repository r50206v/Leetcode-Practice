'''
Runtime: 80ms
Memory Usage: 15.4MB

my solution is based on hashmap
time complexity: O(N)
space complexity: O(N)
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        self.map = {value - k: index for index, value in enumerate(nums)}
        count = 0
        
        for index, value in enumerate(nums):
            
            if self.map.get(value) is not None:
                if self.map[value] != index:
                    del self.map[value]
                    count += 1
                    
        return count

    
    
'''
brute force: two layer of loops 
Time complexity: O(N^2)
Space complexity: O(N)
'''
class Solution:
    def findPairs(self, nums, k):

        s_nums = sorted(nums)

        result = 0

        for i in range(len(s_nums)):
            if (i > 0 and s_nums[i] == s_nums[i - 1]):
                continue
            for j in range(i + 1, len(s_nums)):
                if (j > i + 1 and s_nums[j] == s_nums[j - 1]):
                    continue

                if abs(s_nums[j] - s_nums[i] == k):
                    result += 1

        return result
    
    
'''
Two pointers

1. If it is less than k, we increment the right pointer.
2. If left and right pointers are pointing to the same number, we increment the right pointer too.
3. If it is greater than k, we increment the left pointer.
4. If it is exactly k, we have found our pair, we increment our placeholder result and increment left pointer.

Time Complexity: O(NlogN)
Space Complexity: O(N)
'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # List item 3 in the text
                left += 1
                result += 1
                '''
                this while loop is just to make sure not to count duplicate pairs, 
                so it does not increase the time complexity
                '''
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result
    
    
    
'''
hashmap

time complexity: O(N)
space complexity: O(N)
'''
from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result