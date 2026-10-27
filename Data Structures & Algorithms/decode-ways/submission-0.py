class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = number of ways to decode s[i:]
        dp = [0] * (n + 1)

        # Empty string has 1 valid way
        dp[n] = 1

        for i in range(n - 1, -1, -1):

            # '0' cannot be decoded alone
            if s[i] == '0':
                dp[i] = 0
            else:
                # Decode one digit
                dp[i] = dp[i + 1]

                # Decode two digits
                if i + 1 < n:
                    num = int(s[i:i + 2])

                    if 10 <= num <= 26:
                        dp[i] += dp[i + 2]

        return dp[0]