from heapq import heappop, heappush, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        heapify(min_heap)

        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            else:
                top = heappop(min_heap)
                if top < num:
                    heappush(min_heap, num)
                else:
                    heappush(min_heap, top)

        if len(min_heap) > 0:
            return heappop(min_heap)
        
        return 0