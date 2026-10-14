import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        # Build graph using min-heap
        for start, end in tickets:
            heapq.heappush(graph[start], end)

        result = []

        def dfs(airport):
            # Use all tickets from this airport
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            # Add after using all outgoing tickets
            result.append(airport)

        dfs("JFK")

        # DFS creates the route backwards
        return result[::-1]