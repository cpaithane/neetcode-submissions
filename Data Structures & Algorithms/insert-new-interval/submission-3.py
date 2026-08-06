class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res_list = []
        i = 0
        n = len(intervals)

        # First part
        while i < n and intervals[i][1] < newInterval[0]:
            res_list.append(intervals[i])
            i += 1

        # Merge part, there will be only one newInterval to be merged
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res_list.append(newInterval)

        # Third part
        while i < n:
            res_list.append(intervals[i])
            i += 1

        return res_list