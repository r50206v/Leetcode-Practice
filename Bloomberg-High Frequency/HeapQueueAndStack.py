def ValidParentheses(s):
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


def SlidingWindowMax(nums, k):
    if k == 1:
        return max(nums)

    n = len(nums)
    left = copy.deepcopy(nums)
    right = copy.deepcopy(nums)

    for i in range(1, n):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i-1], nums[i])
        
        j = n - i + 1
        if (j+1) % k == 0:
            right[j] = nums[j]
        else:
            right[j] = max(right[j+1], nums[j])
    output = []
    for i in range(n - k + 1):
        output.append(max(left[i - k + 1], right[i]))
    return output


def TrappingRainWater(height):
    if len(height) < 2:
        return 0
    
    ans = 0
    left_max = [height[0]]
    right_max = [height[-1]]
    for i in range(1, len(height)):
        left_max.append(max(height[i], left_max[i-1]))
    for i in range(len(height) - 2, -1, -1):
        right_max.append(max(height[i], right_max[-1]))
    right_max = right_max[::-1]

    for i in range(len(height)):
        ans += min(left_max[i], right_max[i]) - height[i]
    return ans


def MeetingRoomII(intervals):
    if len(intervals) < 2:
        return len(intervals)

    intervals = sorted(intervals, key=lambda x: x[0])
    ans = [[intervals[0]]]

    for i in range(1, len(intervals)):
        
        curr = intervals[i]
        notAllocate = True
        for j in range(len(ans)):
            if curr[0] >= ans[j][1]:
                ans[j].append(curr)
                notAllocate = False
                break
        if notAllocate:
            ans.append([curr])

    return len(ans)