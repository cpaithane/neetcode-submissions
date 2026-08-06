"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # First simple solution is to use DP.
        # Second is to use min-heap to store end of the interval
        intervals.sort(key = lambda x: x.start)
        min_heap = []
        heapify(min_heap)

        for interval in intervals:
            # Store only overlapping intervals in min_heap. At the end,
            # min_heap will hold overlapping intervals.
            if len(min_heap) > 0 and min_heap[0] <= interval.start:
                heappop(min_heap)

            heappush(min_heap, interval.end)

        return len(min_heap)