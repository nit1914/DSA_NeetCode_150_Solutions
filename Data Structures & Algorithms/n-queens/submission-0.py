class Solution:
    def solveNQueens(self, n: int):
        result = []

        # Track occupied columns and diagonals
        cols = set()
        positive_diag = set()   # row + col
        negative_diag = set()   # row - col

        # Empty chessboard
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            # All queens have been placed
            if row == n:
                solution = ["".join(r) for r in board]
                result.append(solution)
                return

            # Try every column in the current row
            for col in range(n):

                # Check whether this position is attacked
                if col in cols:
                    continue

                if row + col in positive_diag:
                    continue

                if row - col in negative_diag:
                    continue

                # Place queen
                board[row][col] = "Q"

                cols.add(col)
                positive_diag.add(row + col)
                negative_diag.add(row - col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack: remove queen
                board[row][col] = "."

                cols.remove(col)
                positive_diag.remove(row + col)
                negative_diag.remove(row - col)

        backtrack(0)

        return result