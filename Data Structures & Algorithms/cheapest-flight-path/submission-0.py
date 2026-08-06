class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Execute Bellman Ford algorithm
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(0, k+1):
            tmp_prices = prices.copy()

            for flight in flights:
                s = flight[0]
                d = flight[1]
                p = flight[2]

                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < tmp_prices[d]:
                    tmp_prices[d] = prices[s] + p

            prices = tmp_prices

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]