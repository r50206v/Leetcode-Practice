'''
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        avgList = []
        avg = sum(nums[:k]) / k
        avgList.append(avg)
        
        for i in range(k, len(nums), 1):
            newSum = avg * k - nums[i-k] + nums[i]    
            avg = newSum / k
            avgList.append(avg)
            
        return max(avgList)
            
        
'''
Approach #1 Cumulative Sum

Time Complexity: O(n)
Space Complexity: O(n)
'''
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int[] sum = new int[nums.length];
        sum[0] = nums[0];
        for (int i = 1; i < nums.length; i++)
        sum[i] = sum[i - 1] + nums[i];
        double res = sum[k - 1] * 1.0 / k;
        for (int i = k; i < nums.length; i++) {
            res = Math.max(res, (sum[i] - sum[i - k]) * 1.0 / k);
        }
        return res;
    }
}

'''
Approach #2 Sliding Window

Time Complexity: O(n)
Space Complexity: O(1)
'''
public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum=0;
        for(int i=0;i<k;i++)
            sum+=nums[i];
        double res=sum;
        for(int i=k;i<nums.length;i++){
            sum+=nums[i]-nums[i-k];
                res=Math.max(res,sum);
        }
        return res/k;
    }
}

