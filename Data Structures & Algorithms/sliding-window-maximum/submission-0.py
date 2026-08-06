class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Empty heap
        heap = []
        res = []

        # Iterate through the nums array
        for i in range(0, len(nums)):
            # Push val and idx to the max heap
            # The value is negated as we want max heap
            # If not negated, the min heap will kick in.
            heapq.heappush(heap, (-nums[i], i))

            # If size of sliding window matches, pop till the top element
            # is within the sliding window
            if i >= k -1:
                # heap[0][1] => Index at top element
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                # heap[0][0] => Value of top element
                res.append(-heap[0][0])
            
        return res