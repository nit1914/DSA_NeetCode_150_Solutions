import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Adjacency list
        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append((v, t))

        # Distance from k to every node
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min-heap: (time, node)
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)

            # Ignore outdated entry
            if time > dist[node]:
                continue

            # Visit neighbors
            for neighbor, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        # Maximum shortest distance
        answer = max(dist[1:])

        # If any node is unreachable
        if answer == float('inf'):
            return -1

        return answer