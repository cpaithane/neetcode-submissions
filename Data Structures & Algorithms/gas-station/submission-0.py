class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy solution
        # Let's check if there is enough fuel
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0

        for i in range(0, len(gas)):
            # check the total
            total += (gas[i] - cost[i])

            # Reset the total if can't go from this station
            if total < 0:
                start = i + 1
                total = 0

        # No need to go round the array as we know that we have one solution if
        # sufficient gas is present
        return start