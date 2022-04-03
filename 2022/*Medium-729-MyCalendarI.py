'''
brute force:
We will maintain a list of interval events (not necessarily sorted). 
Evidently, two events [s1, e1) and [s2, e2) do not conflict 
if and only if one of them starts after the other one ends: 
    either e1 <= s2 OR e2 <= s1. 
By De Morgan's laws, this means the events conflict when s1 < e2 AND s2 < e1.

time: O(N**2) 
    for each new event, 
    we process every previous event to decide whether the new event can be booked. 
space: O(N)
'''
class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True


'''
we need data structure support sorting and fast insertion

binary tree
time: O(NlogN), worst case O(N**2)
space: O(N)

if search from a sorted array -> binary search using O(logN) to search

'''
class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))



'''
balanced tree
time: O(NlogN)
space: O(N)
'''
import sortedcontainers
class MyCalendar:
    # http://www.grantjenks.com/docs/sortedcontainers/
    def __init__(self):
        self.calendar = sortedcontainers.SortedList()

    def book(self, start: int, end: int) -> bool:
        if not self.calendar:
            self.calendar.add((start, end))
            return True
        
        prev_index = self.calendar.bisect_left((start, end)) - 1
        next_index = self.calendar.bisect_right((start, end))

        if (start, end) in self.calendar:
            return False
        
        if (prev_index == -1 or self.calendar[prev_index][1] <= start) and (next_index == len(self.calendar) or self.calendar[next_index][0] >= end):
            self.calendar.add((start, end))
            return True
        
        return False