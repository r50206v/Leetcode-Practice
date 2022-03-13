'''
caching
nums[left:right+1] = sum[right+1] - sum[left]
sum is the summation of the given index from begining of the list
time: O(N)
space: O(N)
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.mapping = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.mapping[i+1] = self.mapping[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.mapping[right+1] - self.mapping[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



'''
brute force
time: O(N**2)
space: O(1)
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)