from heapq import heappop, heappush, heapify

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Let's maintain max_heap of frequencies.
        max_heap = []
        heapify(max_heap)

        # Let's use deque for entry in max_heap whose freq. is not 0 yet.
        queue = deque()

        # Count the letters
        count_dict = {}
        for task in tasks:
            freq = count_dict.get(task, 0)
            count_dict[task] = freq + 1

        # Push frequencies in the max_heap
        for k, v in count_dict.items():
            heappush(max_heap, -1 * v)

        cycles = 0
        # Till max_heap and queue are not exhausted
        while len(max_heap) > 0 or len(queue) > 0:
            # Increment the cycles
            cycles += 1
            
            # If max_heap has entries, pop it.
            if len(max_heap) > 0:
                freq = -1 * heappop(max_heap)
                freq -= 1

                # Store the non-zero freq. in queue with cycles + n.
                if freq > 0:
                    queue.append((freq, cycles + n))

            else:
                # If max_heap is empty then update the cycle from head of queue
                cycles = queue[0][1]

            # If current cycle matches with the cycles from head of queue
            if queue and queue[0][1] == cycles:
                heappush(max_heap, -1 * queue.popleft()[0])

        return cycles