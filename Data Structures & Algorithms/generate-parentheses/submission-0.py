class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack(open_count, close_count):
            # Base case
            if open_count == n and close_count == n:
                res.append("".join(stack))
                return

            # Add '('
            if open_count < n:
                stack.append("(")

                backtrack(open_count + 1, close_count)

                # Backtrack
                stack.pop()

            # Add ')'
            if close_count < open_count:
                stack.append(")")

                backtrack(open_count, close_count + 1)

                # Backtrack
                stack.pop()

        backtrack(0, 0)
        return res