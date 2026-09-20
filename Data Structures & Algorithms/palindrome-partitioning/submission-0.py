class Solution:
    def partition(self, s: str):
        res = []
        part = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        def backtrack(start):
            # We have used the entire string
            if start == len(s):
                res.append(part.copy())
                return

            # Try every possible substring starting at 'start'
            for end in range(start, len(s)):

                # Only choose it if it is a palindrome
                if isPalindrome(start, end):
                    part.append(s[start:end + 1])

                    # Solve the remaining string
                    backtrack(end + 1)

                    # Undo the choice
                    part.pop()

        backtrack(0)
        return res