class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        INF = float('inf')

        # Cheapest cost to reach each airport
        price = [INF] * n
        price[src] = 0

        # k stops = k + 1 flights
        for _ in range(k + 1):
            # Important: use previous round's values
            temp = price[:]

            for u, v, cost in flights:
                if price[u] != INF:
                    temp[v] = min(temp[v], price[u] + cost)

            price = temp

        return -1 if price[dst] == INF else price[dst]