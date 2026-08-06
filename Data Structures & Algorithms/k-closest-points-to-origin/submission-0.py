from heapq import heappop, heappush, heapify

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_list = []
        heap = []
        heapify(heap)

        for point in points:
            dist = math.sqrt(pow((point[0] - 0), 2) + pow((point[1] - 0), 2))

            if len(heap) < k:
                heappush(heap, ((-1 * dist), point))
            else:
                top_dist, top_point = heappop(heap)
                top_dist = -1 * top_dist

                if top_dist > dist:
                    heappush(heap, ((-1 * dist), point))
                else:
                    heappush(heap, ((-1 * top_dist), top_point))
        
        for info in heap:
            res_list.append(info[1])

        return res_list