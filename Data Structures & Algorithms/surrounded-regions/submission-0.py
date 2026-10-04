class Solution:
    def solve(self, board):
        
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            # Outside the board
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Only process O
            if board[r][c] != 'O':
                return

            # Mark this O as safe
            board[r][c] = '#'

            # Visit 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Start DFS from left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Start DFS from top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Capture surrounded regions
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O':
                    # This O did not touch the border
                    board[r][c] = 'X'

                elif board[r][c] == '#':
                    # This O was connected to the border
                    board[r][c] = 'O'