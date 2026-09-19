class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        path = set()

        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Wrong character or already used
            if board[r][c] != word[i] or (r, c) in path:
                return False

            # Choose
            path.add((r, c))

            # Explore
            found = (
                dfs(r + 1, c, i + 1) or  # down
                dfs(r - 1, c, i + 1) or  # up
                dfs(r, c + 1, i + 1) or  # right
                dfs(r, c - 1, i + 1)     # left
            )

            # Backtrack
            path.remove((r, c))

            return found

        # Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False