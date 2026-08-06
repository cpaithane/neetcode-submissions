from heapq import heapify, heappush, heappop

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Use min heap as we want minimum interval.
        # Sort both intervals and queries
        intervals.sort()
        
        # As the ordering queries matter, use dictionary
        res_dict = {}
        min_heap = []
        i = 0

        # Go through each query
        for q in sorted(queries):
            # Go through intervals
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # Store length of each interval along with end
                heappush(min_heap, (r - l + 1, r))
                i += 1

            # Peak only intervals which are valid. That means, the end
            # from min_heap is less than the q, pop heap.
            while min_heap and min_heap[0][1] < q:
                heappop(min_heap)

            if len(min_heap):
                res_dict[q] = min_heap[0][0]
            else:
                res_dict[q] = -1

        res_list = []
        for q in queries:
            res_list.append(res_dict[q])

        return res_list