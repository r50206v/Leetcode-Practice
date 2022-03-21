'''
time limit exceed
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        last_temp = [(len(temperatures)-1, temperatures[-1])]
        
        for idx in range(len(temperatures)-2, -1, -1):
            
            if temperatures[idx] < last_temp[-1][1]:
                ans[idx] = last_temp[-1][0] - idx
            else: 
                for prev_idx, prev_tmp in last_temp:
                    if temperatures[idx] < prev_tmp:
                        ans[idx] = prev_idx - idx
                    
            last_temp.append((idx, temperatures[idx]))
            
        return ans


'''
monotonic stack
time: O(N)
space: O(N)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer


'''
array + optimized space
time: O(N)
space: O(N)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                # *** THIS WILL MAKE AN EFFECTIVE JUMP TO THE NEAREST HOT DATE
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer