class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            # Non overlapping interval case [1, 2], [3, 4] or [1, 2], [2, 4]
            if interval[0] >= prev_end:
                prev_end = interval[1]
            else:
                # Overlapping case [1, 2], [1, 4]
                prev_end = min(prev_end, interval[1])
                res += 1

        return res