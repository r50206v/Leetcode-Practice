'''
my original answer
Time Limit Exceed
'''

class RecentCounter:

    def __init__(self):
        self.count = []
        self.time = []

    def ping(self, t: int) -> int:
        self.time.append(t)
        currentIndex = len(self.time) - 1
        lowerBound = t - 3000
        
        if lowerBound < 0:
            self.count.append(len(self.time[:currentIndex]) + 1)
        else:
            for i in range(len(self.time)):
                if self.time[i] >= lowerBound:
                    break
            lowerBoundIndex = i
            self.count.append(len(self.time[lowerBoundIndex:currentIndex]) + 1)
            
        return self.count[currentIndex]


'''
dequeue
'''
class RecentCounter:

    def __init__(self):
        self.time = deque()

    def ping(self, t: int) -> int:
        self.time.append(t)
        
        while self.time[0] < self.time[-1] - 3000:
            self.time.popleft()
        
        return len(self.time)