"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)

        for i in range(1, len(intervals)):
            cur = intervals[i - 1]
            next = intervals[i]

            if cur.end > next.start:
                return False

        return True