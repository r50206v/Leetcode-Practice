import collections

def MedianOfTwoSortedArray(nums1, nums2):

    if len(nums1) > len(nums2): 
        return MedianOfTwoSortedArray(nums2, nums1)

    x = len(nums1)
    y = len(nums2)
    low = 0
    high = x
    while low <= high:

        partX = int((low + high)//2)
        partY = int((x + y + 1)//2) - partX

        maxLeftX = nums1[partX - 1] if partX != 0 else float("-inf")
        minRightX = nums1[partX] if partX != 0 else float("inf")

        maxLeftY = nums2[partY - 1] if partY != 0 else float("-inf")
        minRightY = nums2[partY] if partY != 0 else float("inf")

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y)%2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        
        elif maxLeftX > minRightY:
            high = partX - 1
        elif maxLeftY > minRightX:
            low = partX + 1
    

def SearchRotatedSortedArray(nums, target):
    n = len(nums)
    if n == 0:
        return -1
    left = 0
    right = n - 1

    while left <= right:

        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= targe < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def MergeInterval(intervals):
    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals, key=lambda x: x[0])
    ansList = [intervals[0]]

    for i in intervals:

        if i[0] < ansList[-1][1]:
            last = ansList.pop()
            last[1] = max(i[1], last[1])
            ansList.append(last)
        else: 
            ansList.append(i)
    return ansList


def SortCharactersByFreq(s):
    s_count = collections.Counter(s)
    ans = []
    for s, count in s_count.most_common():
        ans.append(s * count)
    return "".join(ans)


def TopKFreqWords(words, k):
    w_count = collections.Counter(words)
    ans = sorted(w_count.items(), key=lambda x: (-x[1], x[0]))
    return [a[0] for a in ans]


def MergeSortedArray(nums1, m, nums2, n):

    while m > 0 or n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1

    if n > 0:
        nums1[:n] = nums[:n]
    

def GroupAnagram(strs):

    ans = collections.defaultdict(list)
    for s in strs:
        anagram = "".join(sorted(s))
        ans[anagram].append(s)

    return ans.items()


def FindAllAnagramString(s, p):
    ns = len(s)
    np = len(p)

    p_count = collections.Counter(p)
    s_count = collections.Counter()
    ans = []
    for i, char in enumerate(s):
        s_count[char] += 1

        if i >= np:
            if s_count[s[i - np]] == 1:
                del s_count[s[i - np]]
            else:
                s_count[s[i - np]] -= 1

        if s_count == p_count:
            ans.append(i)
    return ans


def TwoCityScheduling(costs):
    costs = sorted(costs, key=lambda x: x[1] - x[0])
    midpoint =  len(costs) // 2
    ans = sum([c[1] for c in costs[:midpoint]])
    ans += sum([c[0] for c in costs[midpoint:]])
    return ans