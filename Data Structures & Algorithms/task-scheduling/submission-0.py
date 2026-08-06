from heapq import heappop, heappush, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []
        heapify(max_heap)
        queue = deque()

        count_dict = {}
        for task in tasks:
            freq = count_dict.get(task, 0)
            count_dict[task] = freq + 1

        for k, v in count_dict.items():
            heappush(max_heap, -1 * v)

        cycles = 0
        while len(max_heap) > 0 or len(queue) > 0:
            cycles += 1
            
            if len(max_heap) > 0:
                freq = -1 * heappop(max_heap)
                freq -= 1

                if freq > 0:
                    queue.append((freq, cycles + n))

            else:
                cycles = queue[0][1]

            if queue and queue[0][1] == cycles:
                heappush(max_heap, -1 * queue.popleft()[0])

        return cycles