from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        heapify(heap)
        for v in stones:
            heappush(heap, -1 * v)

        while len(heap) > 1:
            h1 = -1 * heappop(heap)

            if len(heap) > 0:
                h2 = -1 * heappop(heap)
                if h1 != h2:
                    heappush(heap, -1 * (abs(h1 - h2)))

        if len(heap) == 0:
            return 0

        return -1 * heappop(heap)