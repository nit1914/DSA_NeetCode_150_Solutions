from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Put all rotten fruits into queue
        # and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        # Multi-source BFS
        while queue and fresh > 0:
            size = len(queue)

            # Process one complete BFS level = 1 minute
            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries and fresh fruit
                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1):

                        # Fresh -> rotten
                        grid[nr][nc] = 2
                        fresh -= 1

                        # Add for next minute
                        queue.append((nr, nc))

            minutes += 1

        # If fresh fruits remain, they cannot be reached
        if fresh > 0:
            return -1

        return minutes