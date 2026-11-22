
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}

        # Store the last occurrence of each character
        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            # Current partition is complete
            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result
