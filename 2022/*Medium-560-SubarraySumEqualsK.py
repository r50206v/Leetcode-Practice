'''
cumulative sum
time: O(N**2)
space: O(N)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sumList = [0]
        for idx in range(len(nums)):
            sumList.append(sumList[idx] + nums[idx])
            
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if sumList[j] - sumList[i] == k:
                    count += 1
        return count


'''
hashmap
time: O(N)
space: O(N)

Explanation:
The HashMap will store with the key being any particular sum, 
and the value being the number of times it has happened till 
the current iteration of the loop as we traverse the array from left to right.
For example:
k = 26.
If a sub-array sums up to k, then the sum at the end of 
this sub-array will be sumEnd = sumStart + k. 
That implies: sumStart = sumEnd - k.
Suppose, at index 10, sum = 50, and the next 6 numbers are 8,-5,-3,10,15,1.
At index 13, sum will be 50 again (the numbers from indexes 11 to 13 add up to 0).
Then at index 16, sum = 76.
Now, when we reach index 16, sum - k = 76 - 26 = 50. 
So, if this is the end index of a sub-array(s) 
which sums up to k, then before this, just before the start of the sub-array, 
the sum should be 50.
As we found sum = 50 at two places 
before reaching index 16, we indeed have 
two sub-arrays which sum up to k (26): from indexes 14 to 16 and from indexes 11 to 16.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        curr_sum = 0
        mapping = {0: 1}
        
        for idx in range(len(nums)):
            curr_sum += nums[idx]
            
            if mapping.get(curr_sum - k):
                count += mapping[curr_sum - k]
            mapping[curr_sum] = mapping.get(curr_sum, 0) + 1
            
        return count