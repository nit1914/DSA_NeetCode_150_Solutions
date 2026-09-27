
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Check boundaries and water
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0"):
                return

            # Mark land as visited
            grid[r][c] = "0"

            # Explore four directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands