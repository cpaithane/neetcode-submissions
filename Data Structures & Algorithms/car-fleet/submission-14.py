class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nr_cars = len(position)
        pairs = []
        stack = []
        nr_fleets = 0

        for i in range(0, nr_cars):
            pairs.append((position[i], speed[i]))

        # Sort the pairs in descending order
        pairs.sort(reverse=True)
        
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)