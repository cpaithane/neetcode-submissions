from heapq import heapify, heappush, heappop 

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapify(self.min_heap)
        heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, (-1 * num))

        if len(self.max_heap) > len(self.min_heap) + 1:
            top_max = -1 * heappop(self.max_heap)
            heappush(self.min_heap, top_max)

        if len(self.min_heap) > len(self.max_heap) + 1:
            top_min = heappop(self.min_heap)
            heappush(self.max_heap, (-1 * top_min))

    def findMedian(self) -> float:
        min_len = len(self.min_heap)
        max_len = len(self.max_heap)

        if min_len == 0 and max_len == 0:
            return 0

        top_min = 0
        top_max = 0
        if len(self.min_heap) > 0:
            top_min = self.min_heap[0]
        if len(self.max_heap) > 0:
            top_max = -1 * self.max_heap[0]

        print("Max_heap", self.max_heap)
        print("Min_heap", self.min_heap)
        print(top_max, top_min)
        print("\n")

        if max_len > min_len:
            return top_max
        elif min_len > max_len:
            return top_min
        else:
            return ((top_min + top_max) / 2.0)
