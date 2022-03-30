'''
using min heap (data structure)
'''
class SeatManager:

    def __init__(self, n: int):
        # Time: O(N)
        # Space: O(N)
        self.heap = list(range(1, n+1))

    def reserve(self) -> int:
        # Time: O(LogN)
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        # Time: O(LogN)
        heapq.heappush(self.heap, seatNumber)