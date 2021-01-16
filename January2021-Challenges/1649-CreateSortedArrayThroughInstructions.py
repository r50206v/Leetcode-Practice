'''
time limited exceeded
time: O(N**2)
space: O(M)
'''
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        maxElement = max(instructions)
        nums = [0] * (maxElement + 1)
        for e in instructions:
            nums[e] = nums[e] + 1
            cost += min(sum(nums[:e]), sum(nums[e+1:]))
        
        return int(cost % (10e9 + 7))



'''
time: O(Nlog(M))
M is the maximum value in the instructions
space: O(M)
'''
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        # implement Binary Index Tree
        def update(index, value, bit, m):
            index += 1
            while index < m:
                bit[index] += value
                index += index & -index

        def query(index, bit):
            index += 1
            result = 0
            while index >= 1:
                result += bit[index]
                index -= index & -index
            return result

        MOD = 10**9+7
        m = max(instructions)+2
        bit = [0]*m
        cost = 0

        n = len(instructions)
        for i in range(n):
            left_cost = query(instructions[i]-1, bit)
            right_cost = i - query(instructions[i], bit)
            cost += min(left_cost, right_cost)
            update(instructions[i], 1, bit, m)
        return cost % MOD