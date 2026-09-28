
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Base case: water or out of bounds
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0

            # Mark as visited
            grid[r][c] = 0

            # Count current cell and its neighbors
            area = 1
            area += dfs(r + 1, c)  # Down
            area += dfs(r - 1, c)  # Up
            area += dfs(r, c + 1)  # Right
            area += dfs(r, c - 1)  # Left

            return area

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)

        return max_area