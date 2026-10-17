import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Min-heap: (maximum elevation needed, row, col)
        min_heap = [(grid[0][0], 0, 0)]

        visited = set()

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Destination reached
            if r == n - 1 and c == n - 1:
                return time

            # Explore neighbors
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:

                        # We need water level high enough
                        # for both current path and new cell
                        new_time = max(time, grid[nr][nc])

                        heapq.heappush(
                            min_heap,
                            (new_time, nr, nc)
                        )

        return -1