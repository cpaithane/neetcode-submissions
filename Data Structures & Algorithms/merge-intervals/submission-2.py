class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res_list = [] # Stitch the list
        total = len(intervals)

        intervals.sort()
        if total > 0:
            res_list.append(intervals[0])

        print(intervals)

        for interval in intervals:
            last_inserted = res_list[-1]

            if interval[0] <= last_inserted[1]:
                res_list[-1][1] = max(last_inserted[1], interval[1])
            else:
                res_list.append(interval)

        return res_list