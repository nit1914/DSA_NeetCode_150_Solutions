class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        # min_dist[i] = minimum cost to connect point i
        # to any point already in the MST
        min_dist = [float('inf')] * n

        # Start from point 0
        min_dist[0] = 0

        visited = [False] * n
        total_cost = 0

        for _ in range(n):
            # Find the unvisited point with minimum connection cost
            u = -1

            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            # Add this point to MST
            visited[u] = True
            total_cost += min_dist[u]

            # Update distances for remaining points
            for v in range(n):
                if not visited[v]:
                    cost = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])

                    min_dist[v] = min(min_dist[v], cost)

        return total_cost